from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Animal
from django.core.serializers import serialize
from .forms import AnimalForm
from django import forms

def serialized_data(data):
    try:
        return serialize('json', data)
    except:
        return serialize('json', [data])


def read_animals_data(request, animal_id=None):
    if animal_id:
        return get_animal(request, animal_id)
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(request):
    dogs = Animal.objects.filter(kind='D')
    return HttpResponse(serialized_data(dogs))


def get_all_cats(request):
    cats = Animal.objects.filter(kind='C')
    return HttpResponse(serialized_data(cats))


def order_animals(request):
    animals = Animal.objects.all().order_by('age')
    return HttpResponse(serialized_data(animals))


# CRUD operations:

def create_animal_form(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Success!")
            #animals = Animal.objects.all()
            #return render(request, 'list.html', {'animals': animals})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' alert alert-danger'
            return render(request, 'create.html', {'form': form})
    else:
        form = AnimalForm()

    return render(request, 'create.html', {'form': form})


def create_animal(request):
    name = request.GET.get('name')
    breed = request.GET.get('breed')
    age = request.GET.get('age')
    image_url = request.GET.get('image_url')
    description = request.GET.get('description')
    kind = request.GET.get('kind')

    animal = Animal(name=name, age=age, kind=kind, image_url=image_url, description=description, breed=breed)
    animal.save()
    return HttpResponse('Created!')


def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    name = request.GET.get('name')
    animal.name = name
    animal.save()
    return HttpResponse('Edited!')


def delete_animal(request, animal_id):
    Animal.objects.get(pk=animal_id).delete()
    return HttpResponse('Deleted')


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