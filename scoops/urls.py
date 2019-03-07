from django.urls import path, re_path, register_converter
from django.conf.urls import url
from . import views
from .myConverters import CodeConverter 

# app_name = 'scoops'

register_converter(CodeConverter, "mycode")

urlpatterns = [
    path('', views.index),
    path('<year>/', views.test5),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.test6),
    re_path(r'^(?P<alphabet>\w{4})/$', views.test7),
    re_path(r'^(?P<alphabet>[a-z]{4})/(?P<alphabet2>[a-z]{2})/$', views.test8),
    path('article/<int:year>/<int:month>/<slug:myname>/', views.func1),
    path('article5/<mycode:num>/', views.func2)
]