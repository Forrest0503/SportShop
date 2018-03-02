from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'SportShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'User.views.login'),
    url(r'^signup/', 'User.views.signup'),
    url(r'^manager_login/', 'User.views.manager_login'),
    url(r'^manager_signup/', 'User.views.manager_signup'),
    # url(r'^login_page/', 'User.views.login_page'),
    # url(r'^login_submit/?', 'User.views.login_submit'),
    # url(r'^signup_page/', 'User.views.signup_page'),
    # url(r'^signup_submit/?', 'User.views.signup_submit'),
    url(r'^logout/', 'User.views.logout'),
    url(r'^manager_logout/', 'User.views.manager_logout'),
    url(r'^redirect_to_login_page/$', RedirectView.as_view(url='/User/login', permanent=False)),
    url(r'^redirect_to_manager_login_page/$', RedirectView.as_view(url='/User/manager_login', permanent=False)),
    url(r'^redirect_to_home_page/$', RedirectView.as_view(url='/Goods/home_page', permanent=False)),
    
]
