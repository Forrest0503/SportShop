from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'SportShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^goods_manage?', 'Manager.views.goods_manage'),
    url(r'^orders_manage', 'Manager.views.orders_manage'),
    url(r'^order_detail', 'Manager.views.order_detail'),
    url(r'^redirect_to_manager_login_page/$', RedirectView.as_view(url='/User/manager_login', permanent=False)),
    url(r'^redirect_to_goods_manager_page/$', RedirectView.as_view(url='/Manager/goods_manager', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
