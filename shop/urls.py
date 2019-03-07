from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('<id2>/detail/', views.article_detail, name="detail"),
    path('reversetest/', views.article_reversetest, name="reversetest2"),
    path('temptest/', views.template_test, name='ttest'),
    path('insert/', views.article_insert, name="insert"),
    path('update/', views.article_update, name="update"),
    path('delete/', views.article_delete, name="delete"),
    path('test1/', views.test1, name="reversetest1"),
    path('test2/', views.test2),
    path('test3/', views.test3),
]