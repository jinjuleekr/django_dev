from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('', views.favorite_list, name="list"),
    path('thing/', views.FavoriteThingLV.as_view(), name="favoriteList"),
    path('thing/<pk>/', views.FavoriteThingDV.as_view(), name="favoriteDetail"),
    path('food/', views.FoodLV.as_view(), name="foodList"),
    path('food/<pk>/', views.FoodDV.as_view(), name="foodDetail"),
    path('movie/', views.MovieLV.as_view(), name="movieList"),
    path('movie/<pk>/', views.MovieDV.as_view(), name="movieDetail"),
]