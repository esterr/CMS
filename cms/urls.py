from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^type/', include('tmpls_types.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^template/', include('tmpls.urls')),
)
