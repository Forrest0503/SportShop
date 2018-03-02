#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db import models
from models import User, Manager
from Utils.UserUtil import *
import time

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {}
        context.update(csrf(request))
        try:
            user = User.objects.get(name=username)
            if user.password == password:
                context['success'] = '登录成功'
                response = HttpResponseRedirect('/User/redirect_to_home_page')
                #设置cookie
                response.set_cookie('username', username, 3600)
                return response
            else:
                context['error'] = '密码错误'
                return render(request, "login.html", context)
        except Exception, e:
            print e
            context['error'] = '用户不存在'
            return render(request, "login.html", context) 

def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        localtime = time.localtime(time.time())
        formated_time = time.strftime("%Y-%m-%d", localtime) 
        context = {}
        context.update(csrf(request))
        if username == '' or password1 == '' or password2 == '':
            context['error'] = '必填项不能为空'
            return render(request, 'register.html', context=context)
        if not password1 == password2:
            context['error'] = '两次输入密码不一致'
            return render(request, 'register.html', context=context)
        try:
            u = User.objects.get(name=username)
        except:
            try:
                user = User(name=username, password=password1, deleted=0, registration_date=formated_time, telephone=phone, address=address)
                user.save()
                context['success'] = "注册成功"
                response = render(request, 'register.html', context)
                #设置cookie
                response.set_cookie('username', username, 3600)
                return response
            except:
                context['error'] = "长度不符合要求"
                return render(request, 'register.html', context)
        else:
            context['error'] = "用户名已存在"
            return render(request, 'register.html', context)


def manager_login(request):
    if request.method == 'GET':
        return render(request, 'manager_login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {}
        context.update(csrf(request))
        try:
            manager = Manager.objects.get(name=username)
            if manager.password == password:
                context['success'] = '登录成功'
                response = HttpResponseRedirect('/Manager/goods_manager')
                #设置cookie
                response.set_cookie('manager_username', username, 3600)
                return response
            else:
                context['error'] = '密码错误'
                return render(request, "manager_login.html", context)
        except Exception, e:
            print e
            context['error'] = '用户不存在'
            return render(request, "manager_login.html", context)

def manager_signup(request):
    if request.method == 'GET':
        return render(request, 'manager_register.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        context = {}
        context.update(csrf(request))
        if username == '' or password1 == '' or password2 == '':
            context['error'] = '必填项不能为空'
            return render(request, 'manager_register.html', context=context)
        if not password1 == password2:
            context['error'] = '两次输入密码不一致'
            return render(request, 'manager_register.html', context=context)
        try:
            u = Manager.objects.get(name=username)
        except:
            try:
                manager = Manager(name=username, password=password1)
                manager.save()
                context['success'] = "注册成功"
                response = render(request, 'manager_register.html', context)
                #设置cookie
                response.set_cookie('manager_username', username, 3600)
                return response
            except Exception, e:
                print e
                context['error'] = "长度不符合要求"
                return render(request, 'manager_register.html', context)
        else:
            context['error'] = "用户名已存在"
            return render(request, 'manager_register.html', context)