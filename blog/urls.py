from django.urls import path, re_path #django 2.xx version
from django.conf.urls import url #django 1.xx version
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.get_redirect1),
    path('google/', views.get_redirect2),
    path('postlist/', views.post_list, name="list"),
    path('<int:post_id>/', views.post_detail, name="detail"),
    path('json/', views.json_test, name="jsontest"),
    path('exceldown/', views.excel_download),
    path('csvdown/', views.pandas_csv),
    path('aa/', views.test1),
    path('bb/', views.test2),
    # All the param named as <year>
    url(r'^article/(?P<year>[0-9]{4})/$', views.test3),
    re_path(r'^article2/(?P<year>[0-9]{4})/$', views.test4),
    path('article3/<year>/', views.test5),              #path 쓰는 것을 권장!
    url(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.test6),
]

