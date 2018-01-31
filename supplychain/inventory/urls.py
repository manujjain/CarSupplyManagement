from django.conf.urls import url,include
from django.contrib import admin
from .views import carcreation

urlpatterns = [
    url(r'^add/$', carcreation),
    
   ]
