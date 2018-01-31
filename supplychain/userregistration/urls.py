from django.conf.urls import url,include
from django.contrib import admin
from .views import Usercreation, home, get_query, login_page

urlpatterns = [
    url(r'^manufacturer$', Usercreation.as_view()),
    url(r'^success/$',home,name='success'),
    url(r'^detail$',get_query),
    url(r'^login$',login_page),
]

