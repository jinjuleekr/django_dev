from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import FavoriteThing, Food, Movie

def favorite_list(request):
    flist = FavoriteThing.objects.all()
    return render(request, "favorite/thing.html", {"favorite_list":flist})

class FavoriteThingLV(ListView):
    template_name = 'favorite/thing.html'
    context_object_name = 'thing_list'

    def get_queryset(self):
        return FavoriteThing.objects.order_by('title')

class FavoriteThingDV(DetailView):
    model = FavoriteThing
    context_object_name = 'thing'
    template_name = 'favorite/thing_detail.html'

class FoodLV(ListView):
    template_name = 'favorite/thing.html'
    context_object_name = 'food_list'
    
    def get_queryset(self):
        return Food.objects.order_by('food')

class FoodDV(DetailView):
    model = Food
    context_object_name = 'food'
    template_name = 'favorite/thing_detail.html'

class MovieLV(ListView):
    template_name = 'favorite/thing.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.order_by('movie')

class MovieDV(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'favorite/thing_detail.html'