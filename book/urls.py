from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name="list"),
    path('detail/<pk>/', views.book_detail, name="detail"),
    path('update/<pk>/', views.book_update, name="update"),
    path('insert/', views.book_insert, name="insert"),
    path('delete/<pk>/', views.book_delete, name="delete"),
    path('searchData/', views.searchData, name="search")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)