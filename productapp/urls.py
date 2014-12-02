#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('productapp.views',
    url(r'^hello/$', 'hello'),
    url(r'^communities/$', 'list_communities', name='list_communities'),
    url(r'^list-all/(?P<community_id>\d+)/$', 'list_product', name='list_product'),
    url(r'^view/(?P<product_id>\d+)/$', 'view_product', name='view_product'),
    url(r'^ajax_deal/$', 'ajax_deal', name='ajax_deal'),
)