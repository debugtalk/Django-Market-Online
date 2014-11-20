from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from Django_Config import views

urlpatterns = patterns('Django_Config.views',
    url(r'^hello/$', 'hello'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^product/', include('productapp.urls', namespace='productapp'), name='productapp'),
)

urlpatterns += patterns('',
    url(r'^cart/', include('cartapp.urls', namespace='cartapp'), name='cartapp'),
)

'''
urlpatterns += patterns('',
    url(r'^market/', include('marketapp.urls', namespace='marketapp'), name='marketapp'),
)
'''
#urlpatterns += staticfiles_urlpatterns()