from django.db import models

class FavoriteThing(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    url =models.URLField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']

class Food(models.Model):
    food = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length =20, blank=True, null=True)

    def __str__(self):
        return self.food


class Movie(models.Model):
    movie = models.CharField(max_length=25, blank=True, null=True)
    character = models.CharField(max_length=30, blank=True, null=True)
    genre = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.movie
