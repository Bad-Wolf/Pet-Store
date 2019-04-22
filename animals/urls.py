from django.urls import path, re_path
from . import views
app_name = "animals"

urlpatterns = [
    path('all/', views.AnimalList.as_view(), name='all'),
    path('all/<int:animal_id>/', views.get_animal, name='animal_id'),
    path('all/dogs/', views.get_all_dogs, name='dogs'),
    path('all/cats/', views.get_all_cats, name='cats'),
    path('all/ordered/', views.order_animals, name='ordered'),
    path('create/', views.AnimalCreate.as_view(), name='create'),
    path('edit/<int:pk>/', views.AnimalUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', views.AnimalDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', views.AnimalDetail.as_view(), name='detail'),
]