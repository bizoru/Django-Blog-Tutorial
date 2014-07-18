from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogsite.views.home', name='home'),
    url(r'^blog/', include('blogsite.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
