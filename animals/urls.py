from django.urls import path, re_path
from . import views
app_name = "animals"

urlpatterns = [
    path('all/', views.AnimalList.as_view(), name='all'),
    path('create/', views.AnimalCreate.as_view(), name='create'),
    path('edit/<int:pk>/', views.AnimalUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', views.AnimalDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', views.AnimalDetail.as_view(), name='detail'),
]