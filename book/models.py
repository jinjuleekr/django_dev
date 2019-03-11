from django.db import models
from django.shortcuts import reverse
from django import forms
from django.core.validators import MinLengthValidator

def min_length10_validator(value):
    if len(value) <10:
        raise forms.ValidationError("10자리 이상만 입력!")

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    publisher = models.CharField(max_length=50, validators=[min_length10_validator])
    publication_date = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=15)
    photo = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True, upload_to="book")
    photo3 = models.ImageField(blank=True, upload_to='book/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:list')

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'ip','photo','photo2','photo3']
        labels = {'title':'ModelForm책제목',
                    'author':"ModelForm저자",
                    'publisher':'ModelForm출판사'}
        help_texts = {'author':'작가 이름을 3자리 이상 입력!',
                        'ip':'ip 주소는 자동으로 입력 됨'}



