from django.conf.urls import patterns, include, url
from django.contrib import admin
from general_api import views as general_api_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\w+)/(\w+)/(\w+)/(\w+)', csrf_exempt(general_api_views.APIView.as_view())),
    url(r'^(\w+)/(\w+)/(\w+)', csrf_exempt(general_api_views.APIView.as_view())),
    url(r'^(\w+)/(\w+)/', csrf_exempt(general_api_views.APIView.as_view())),
)
