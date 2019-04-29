from django.urls import path, include
from . import views

urlpatterns = [path('', views.BookView.as_view(), name='books'),
               path('<pk>/', views.BookDetail.as_view(), name='book-detail'),
               path('mine/', views.UserBooks.as_view(), name='user-books'),
               ]