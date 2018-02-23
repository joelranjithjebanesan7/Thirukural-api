from django.conf.urls import url
from thirukural import views as thirukural_views
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^thirukurals/$', thirukural_views.kural_list, name = 'thirukural-list'),
    
    ]