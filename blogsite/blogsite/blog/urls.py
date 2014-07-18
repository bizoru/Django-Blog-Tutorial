from django.conf.urls.defaults import *
from blogsite.blog.views import archive

urlpatterns = patterns('',url(r'^$',archive))
