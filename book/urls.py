from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name="list"),
    path('detail/<pk>/', views.book_detail, name="detail"),
    path('update/<pk>/', views.book_update, name="update"),
    path('insert/<pk>/', views.book_insert, name="insert"),
    path('delete/<pk>/', views.book_delete, name="delete"),
]