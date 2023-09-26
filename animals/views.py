import datetime

from django.shortcuts import render, redirect
from animals.models import Animal, Schedule
from animals.schedule_calculations import time_to_visit


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
    date_main = []
    schedule_time = Schedule.objects.all().filter(animal_id=animal_id)
    for item in schedule_time:
        date_list = [item.start_time, item.end_time]
        date_main.append(date_list)
    print(date_main)
    if not date_main:
        date_main = False
    if request.method == 'POST':
        times = time_to_visit(date_main, request.POST['val'][0])
        print(times)
        return render(request, 'animals/schedule.html', {'res': times})
    return render(request, 'animals/animal.html', {'result': animal_data, 'reserved_time': date_main})


def search(request):
    if request.method == 'POST':
        data = request.POST
        data_animal = Animal.objects.get(name=data['search'])
        return render(request, 'animals/search.html', {'result': data_animal})


def schedule(request, animal_id):
    return render(request, 'animals/schedule.html', {})