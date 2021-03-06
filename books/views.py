from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Book, Author


class BookView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetail(LoginRequiredMixin, generic.DetailView):
    loging_url = '/accounts/login/'
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class UserBooks(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        user_id = int(self.request.user.id)
        try:
            author = Author.objects.all().filter(user__pk=user_id)[0]
            books = Book.objects.all().filter(author=author.pk)
            return books
        except:
            return []