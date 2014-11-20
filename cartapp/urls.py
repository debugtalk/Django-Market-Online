#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('cartapp.views',
    url(r'^view/$', 'view_cart', name='view_cart'),
    url(r'^add/(?P<product_id>\d+)/$', 'add_to_cart', name='add_to_cart'),
    url(r'^clean/$', 'clean_cart', name='clean_cart'),
)
