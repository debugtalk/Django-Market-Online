#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('cartapp.views',
    url(r'^show/$', 'show_cart', name='show_cart'),
    url(r'^add/$', 'add_product_to_cart', name='add_product_to_cart'),
    url(r'^remove-category/(?P<product_id>\d+)/$', 'remove_productCategory_from_cart', name='remove_productCategory_from_cart'),
    url(r'^remove-single/$', 'remove_prodcutItem_from_cart', name='remove_prodcutItem_from_cart'),
    url(r'^clear/$', 'clear_cart', name='clear_cart'),
    url(r'^update-quantity/$', 'update_quantity', name='update_quantity'),
    url(r'^total-price/$', 'get_cart_total_price', name='get_cart_total_price'),
    url(r'^log-user-info/$', 'log_user_info', name='log_user_info'),
    url(r'^success/$', 'order_successfully', name='order_successfully'),
    url(r'^confirm-order/$', 'confirm_order', name='confirm_order'),
)
