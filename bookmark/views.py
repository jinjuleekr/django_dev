from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark #object_list를 가지고, bookmark_list.html로
class BookmarkDV(DetailView):
    model = Bookmark #object

    