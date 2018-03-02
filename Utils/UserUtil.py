#coding=utf8
from django.db import models
from User.models import User, Manager
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def test_cookie(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        #登录已过期
        response = HttpResponseRedirect('/User/redirect_to_login_page')
        return response
    try:
        user = User.objects.get(name=username)
    except:
        response = HttpResponseRedirect('/User/redirect_to_login_page')
        return response
    return username, user

def manager_test_cookie(request):
    if 'manager_username' in request.COOKIES:
        username = request.COOKIES['manager_username']
    else:
        #登录已过期
        response = HttpResponseRedirect('/User/redirect_to_manager_login_page')
        return response
    try:
        manager = Manager.objects.get(name=username)
    except:
        response = HttpResponseRedirect('/User/redirect_to_manager_login_page')
        return response
    return username, manager

def logout(request):
    response = HttpResponseRedirect('/User/redirect_to_login_page')
    response.delete_cookie('username')
    return response

def manager_logout(request):
    response = HttpResponseRedirect('/User/redirect_to_manager_login_page')
    response.delete_cookie('manager_username')
    return response