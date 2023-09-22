from django.shortcuts import render, redirect
from animals.models import Animal


def animals(request):
    data = request.GET
    all_animals = Animal.objects.all()
    if data:
        if data['sort_by']:
            all_animals = all_animals.all().filter().order_by(data['sort_by'])
    result = all_animals
    return render(request, 'animals/animals.html', {'animals': result})


def animal(request, animal_id):
    animal_data = Animal.objects.get(id=animal_id)
    return render(request, 'animals/animal.html', {'result': animal_data})


def search(request):
    if request.method == 'POST':
        data = request.POST
        data_animal = Animal.objects.get(name=data['search'])
        return render(request, 'animals/search.html', {'result': data_animal})


def schedule(request, animal_id):
    return render(request, 'animals/schedule.html', {})