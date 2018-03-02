# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db import models
from User.models import User, Manager
from Manager.models import Commodity
from Goods.models import Shopping, Order, OrderDetail
from Utils.UserUtil import *
import time
# Create your views here.
def goods_manage(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        return HttpResponseRedirect('/User/redirect_to_manager_login_page/')
    #删除商品
    if request.method == 'GET':
        all_goods = Commodity.objects.all()
        context['all_goods'] = all_goods
        if request.GET.get('id'):
            try:
                commodity_id = request.GET.get('id')
                commodity = Commodity.objects.get(id=commodity_id)
                commodity.delete()
                shopping = Shopping.objects.filter(commodity_id=commodity_id)
                shopping.delete()
            except Exception, e:
                print e
                context['error'] = e
            # return render(request, 'goods_manager.html', context)
            return HttpResponseRedirect('/Manager/goods_manage')
        else:
            return render(request, 'goods_manage.html', context)
    # 添加商品
    if request.method == 'POST':
        if request.POST.has_key('add'):
            name = request.POST.get('name')
            classify = request.POST.get('classify')
            color = request.POST.get('color')
            size = request.POST.get('size')
            price = request.POST.get('price')
            inventory = request.POST.get('inventory')
            detail = request.POST.get('detail')
            localtime = time.localtime(time.time())
            formated_time = time.strftime("%Y-%m-%d", localtime) 

            if name == '' or price == None or inventory == None or detail == '':
                context['error'] = '必填项不能为空'
                return render(request, 'goods_manage.html', context)

            try:
                picture = request.FILES['picture']
            except:
                context['error'] = ' 图片上传失败'
                return render(request, 'goods_manage.html', context)

            try:
                new_commodity = Commodity(
                    name=name, 
                    classify=classify, 
                    color=color, 
                    size=size, 
                    price=price, 
                    inventory=inventory, 
                    picture=picture, 
                    detail=detail,
                    onsale_time=formated_time,
                    deleted=0
                )
                print size, color
                new_commodity.save()
                context['success'] = '添加商品成功'
            except Exception, e:
                print e
                context['error'] = e
        return HttpResponseRedirect('/Manager/goods_manage')

# def goods_delete(request):
#     context = {}
#     if request.method = "GET":
        
#         return render(request, 'goods_manager.html', context)

def orders_manage(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        return HttpResponseRedirect('/User/redirect_to_manager_login_page')

    #发货
    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        order = Order.objects.get(id=order_id)
        order.state = "待确认收货"
        order.save()
        return HttpResponseRedirect('/Manager/orders_manage')
        
    orders = Order.objects.all()
    order_detail_list = []
    for order in orders:
        order_details = OrderDetail.objects.filter(order_id=order.id)
        order_detail_list.append(order_details)
    
    context['orders'] = zip(orders, order_detail_list)

    return render(request, 'orders_manage.html', context)

def order_detail(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        return HttpResponseRedirect('/User/redirect_to_manager_login_page')

    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        order = Order.objects.get(id=order_id)
        order_detail = OrderDetail.objects.filter(order_id=order_id)
        context['order_detail'] = order_detail
        context['order'] = order
    return render(request, 'order_detail.html', context)