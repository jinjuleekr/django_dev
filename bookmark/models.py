from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title'] #title 기본값은 오름차순, -title은 내림차순
