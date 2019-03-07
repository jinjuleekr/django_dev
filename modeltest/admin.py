from django.contrib import admin
from .models import Reporter, Article, Publication, Place, Restaurant, Waiter

admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)