#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('cartapp.views',
    url(r'^show/$', 'show_cart', name='show_cart'),
    url(r'^add/$', 'add_product_to_cart', name='add_product_to_cart'),
    url(r'^remove-category/$', 'remove_productCategory_from_cart', name='remove_productCategory_from_cart'),
    url(r'^remove-single/$', 'remove_prodcutItem_from_cart', name='remove_prodcutItem_from_cart'),
    url(r'^clear/$', 'clear_cart', name='clear_cart'),
    url(r'^set-quantity/$', 'set_quantity', name='set_quantity'),
)
