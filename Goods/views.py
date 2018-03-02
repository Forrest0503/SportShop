# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db import models
from User.models import User
from Manager.models import Commodity
from Goods.models import Shopping, Order, OrderDetail
from Utils.UserUtil import *
from Utils.SearchEngine import *
import time
import random
import difflib

# Create your views here.
def home_page(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        pass
    
    if request.method == "GET":
        all_goods = Commodity.objects.all().exclude(pk__in=[42,24,15])
        context['goods'] = all_goods
        context['carousel_goods'] = Commodity.objects.filter(pk__in=[42,24,15])
        return render(request, 'home_page.html', context)

def search(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        pass
    if 'query_name' not in request.POST:
        return HttpResponseRedirect('/Goods/home_page', context)
    query_name = request.POST.get('query_name')
    goods_all = Commodity.objects.all()
    goods_similar = []  #相似商品列表
    sim_list = []  #相似度列表
    engine = SearchEngine()  
    for each in goods_all:
        sim = engine.similarity(query_name, each.name)
        if sim > 0.25:
            goods_similar.append(each)
            sim_list.append(sim)

    goods_tuple = zip(goods_similar, sim_list)
    goods_tuple = sorted(goods_tuple, key=lambda x: -x[1])
    print goods_tuple
    goods_list = []  #排序后的商品列表
    for each in goods_tuple:
        goods_list.append(each[0])
    context['goods'] = goods_list
    if len(goods_list) == 0:
        context['empty'] = True
    return render(request, 'search_list.html', context)
    
def good_detail(request):
    context = {}
    try:
        commodity_id = request.GET.get('id')
        commodity = Commodity.objects.get(id=commodity_id)
        context['good'] = commodity

        if not commodity.color == '':
            color = commodity.color.encode('utf8').split(',')
            context['color'] = color

        if not commodity.size == '':
            size = commodity.size.encode('utf8').split(',')
            context['size'] = size
    except:
        pass
        # return HttpResponseRedirect('/Goods/home_page')

    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        pass

    return render(request, 'goods_detail.html', context)
    
def add_to_cart(request):
    context = {}
    try:
        username, user = test_cookie(request)
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page')
            
    user_id = request.GET.get('user_id')
    commodity_id = request.GET.get('commodity_id')
    color = request.POST.get('color')
    size = request.POST.get('size')
    quantity = request.POST.get('quantity')
    try:
        shopping = Shopping.objects.get(user_id=user_id, commodity_id=commodity_id, color=color, size=size)
        shopping.quantity = shopping.quantity + int(quantity)
        shopping.save()
    except Exception, e:
        print e
        try:
            new_shopping = Shopping(
                user_id=user_id, 
                commodity_id=commodity_id, 
                quantity=quantity,
                color = color,
                size=size
            )
            new_shopping.save()
        except:
            # context['error']
            pass
    return render(request, 'add_to_cart.html', context)

def remove_from_cart(request):
    shopping_id = request.GET.get('shopping_id')
    try:
        shopping = Shopping.objects.get(id=shopping_id)
        shopping.delete()
    except Exception, e:
        print e
    return HttpResponseRedirect('cart.html')
    

def cart(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user

        # 展示购物车
        try:
            good_list = []
            total_price = 0.0
            all_shopping = Shopping.objects.filter(user_id=user.id)
            for each in all_shopping:
                good = Commodity.objects.get(id=each.commodity_id)
                good_list.append(good)
                print good.picture.url
                total_price = total_price + good.price * each.quantity
            if user.address:
                context['address'] = user.address
            if user.telephone:
                context['phone'] = user.telephone
            context['good_list'] = zip(all_shopping, good_list)
            context['total_price'] = total_price
        except Exception, e:
            print e

        # 创建订单
        if request.method == 'POST':
            total_price = request.GET.get('total_price')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            print address
            if address == None:
                address = user.address
            if phone == None:
                phone = user.telephone
            localtime = time.localtime(time.time())
            formated_time = time.strftime("%Y-%m-%d", localtime) 
            #建Order表
            try:
                new_Order = Order(
                    user_id=user.id, 
                    total_price=total_price, 
                    receiver_name=user.name,
                    telephone=phone,
                    address=address, 
                    date=formated_time,
                    state='未发货',
                )
                new_Order.save()
            except Exception, e:
                print e
            #建OrderDetail表
            try:
                all_shopping = Shopping.objects.filter(user_id=user.id)
                for each in all_shopping:
                    good = Commodity.objects.get(id=each.commodity_id)
                    if good.inventory < each.quantity:
                        new_Order.delete()
                        context['error'] = '商品数量不足'
                        return render(request, 'cart.html', context)
                    new_OrderDetail = OrderDetail(
                        order_id=new_Order.id,
                        commodity_id=good.id,
                        commodity_name=good.name,
                        pic_url=good.picture.url,
                        receiver_name=user.name,
                        color=each.color,
                        size=each.size,
                        buying_price=good.price*each.quantity,
                        quantity=each.quantity,
                    )
                    good.inventory = good.inventory - each.quantity
                    good.save()
                    new_OrderDetail.save()
                    each.delete()
                context['good_list'] = None
                context['total_price'] = 0.0;
            except Exception, e:
                print e
            return HttpResponseRedirect('/Goods/order_success')

    except: #未登录
        return HttpResponseRedirect('/User/redirect_to_login_page')

    return render(request, 'cart.html', context)

def cancel_order(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return HttpResponseRedirect('/User/login')

    order_id = request.GET.get('order_id')
    try:
        order = Order.objects.get(id=order_id)
        order_details = OrderDetail.objects.filter(order_id=order_id)
        order_details.delete()
        order.delete()
        
    except Exception, e:
        print e
    return HttpResponseRedirect('order.html', context)
    
def good_list(request):
    name = request.GET.get('name')
    context = {}
    classify = request.GET.get('classify')
    goods = Commodity.objects.filter(classify=classify).exclude(pk__in=[42,24,15])
    context['goods'] = goods
    context['classify'] = classify
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return render(request, 'goods_list.html', context)
    return render(request, 'goods_list.html', context)
    

def order_success(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
        return render(request, 'order_success.html', context)
    except:
        return render(request, 'order_success.html', context)

def editInfo(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        pass

    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        try:
            user.telephone = phone
            user.address = address
            user.save()
        except Exception, e:
            print e
    return render(request, 'editInfo.html', context)

def order(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return HttpResponseRedirect('/User/login')

    #收货
    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        order = Order.objects.get(id=order_id)
        order.state = "订单已完成"
        order.save()
        return HttpResponseRedirect('/Goods/order')

    #获取未完成订单
    orders = Order.objects.filter(user_id=user.id).exclude(state='订单已完成')
    order_detail_list = []
    for order in orders:
        order_details = OrderDetail.objects.filter(order_id=order.id)
        order_detail_list.append(order_details)
    context['orders'] = zip(orders, order_detail_list)

    #获取已完成订单
    closed_orders = Order.objects.filter(user_id=user.id, state='订单已完成')
    closed_order_detail_list = []
    for order in closed_orders:
        closed_order_details = OrderDetail.objects.filter(order_id=order.id)
        closed_order_detail_list.append(closed_order_details)
    context['closed_orders'] = zip(closed_orders, closed_order_detail_list)

    return render(request, 'order.html', context)