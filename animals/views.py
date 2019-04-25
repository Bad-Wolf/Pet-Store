from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Animal
from .forms import AnimalForm


class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animals'


class AnimalUpdate(UpdateView):
    model = Animal
    template_name = 'create.html'
    form_class = AnimalForm
    success_url = '/animals/all/'


class AnimalCreate(CreateView):
    model = Animal
    template_name = 'create.html'
    form_class = AnimalForm
    success_url = '/animals/all/'


class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/animals/all/'


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'animal_detail.html'