#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('productapp.views',
    url(r'^hello/$', 'hello'),
    url(r'^list/$', 'list_product', name='list_product'),
    url(r'^view/(?P<id>\d+)/$', 'view_product', name='view_product'),
)