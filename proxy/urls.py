from django.conf.urls.defaults import *

urlpatterns = patterns('deproxy.proxy.views',
    (r'^$', 'index'),
    (r'^render/$', 'render'),
)
