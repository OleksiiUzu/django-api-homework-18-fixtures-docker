from django.shortcuts import render
from animals.models import Animal, Schedule
from animals.schedule_calculations import time_to_visit


def taking_reserve_dates(animal_id):
    date_main = []
    schedule_time = Schedule.objects.all().filter(animal_id=animal_id)
    for item in schedule_time:
        start_time = item.start_time.replace(tzinfo=None)
        end_time = item.end_time.replace(tzinfo=None)
        date_list = [start_time, end_time]
        date_main.append(date_list)
    if not date_main:
        date_main = False
    return date_main


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
    reserve_dates = taking_reserve_dates(animal_id)
    return render(request, 'animals/animal.html', {'result': animal_data, 'reserved_time': reserve_dates})


def search(request):
    if request.method == 'POST':
        data = request.POST
        data_animal = Animal.objects.get(name=data['search'])
        return render(request, 'animals/search.html', {'result': data_animal})


def schedule(request, animal_id):
    reserve_dates = taking_reserve_dates(animal_id)
    if request.method == 'POST':
        times = time_to_visit(int(request.POST['val'][0]), reserve_dates)
        return render(request, 'animals/schedule.html', {'res': times})
    return render(request, 'animals/schedule.html', {})
