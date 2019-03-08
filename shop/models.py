from django.db import models
from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):

    name = models.TextField() #null 허용하지 않음
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shop_post_set')
    
STATUS_CHOICES = (
('d', 'Draft'),
('p', 'Published'),
('w', 'Withdrawn'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.title

    class Meta: #sort를 간편하게 하는 방법
        ordering = ['-id'] # ascending

    def get_absolute_url2(self):
        print(self)
        return reverse('shop:detail', args=[self.id])

    # success_url이 없으면 자동 호출 됨
    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={"pk":self.id})