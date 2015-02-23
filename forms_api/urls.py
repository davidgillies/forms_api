from django.conf.urls import patterns, include, url
from django.contrib import admin
from general_api import views as general_api_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\w+)/(\w+)/(\w+)/(\w+)', general_api_views.Index.as_view()),
    url(r'^(\w+)/(\w+)/(\w+)', general_api_views.Index.as_view()),
    url(r'^(\w+)/(\w+)/', general_api_views.Index.as_view()),
)
