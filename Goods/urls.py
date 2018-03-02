from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'SportShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^good_detail?', 'Goods.views.good_detail'),
    url(r'^good_list', 'Goods.views.good_list'),
    url(r'^add_to_cart', 'Goods.views.add_to_cart'),
    url(r'^remove_from_cart', 'Goods.views.remove_from_cart'),
    url(r'^cart', 'Goods.views.cart'),
    url(r'^cancel_order', 'Goods.views.cancel_order'),
    url(r'^order_success', 'Goods.views.order_success'),
    url(r'^editInfo', 'Goods.views.editInfo'),
    url(r'^order', 'Goods.views.order'),
    url(r'^logout/', 'User.views.logout'),
    url(r'^redirect_to_good_detail_page/$', RedirectView.as_view(url='/Goods/good_detail', permanent=False)),
    url(r'^home_page', 'Goods.views.home_page'),
    url(r'^search', 'Goods.views.search'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
