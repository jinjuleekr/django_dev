from django.contrib import admin
from .models import FavoriteThing, Food, Movie

# Register your models here.
admin.site.register(FavoriteThing)
admin.site.register(Food)
admin.site.register(Movie)