from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

class BookListView(ListView):
    model = Book
    paginate_by =10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mymessage"] = "ListView상속"
        context["today"] = timezone.now()
        context["keyword"] = self.request.GET.get('page', '')

book_list = ListView.as_view(model=Book, paginate_by=10)
book_detail = DetailView.as_view(model=Book)
book_insert = CreateView.as_view(model=Book, fields="__all__")
book_update = UpdateView.as_view(model=Book, fields="__all__")
book_delete = DeleteView.as_view(model=Book, success_url="/book/")