from django.shortcuts import render


def animals(request):
    return render(request, 'animals/animals.html', {})


def animal(request, animal_id):
    result = animal_id
    print(result)
    return render(request, 'animals/animal.html', {'result': result})


def animal_sort(request, sort_by):
    result = sort_by
    return render(request, 'animals/sort_animal.html', {'result': result})


def search(request):
    return render(request, 'animals/search.html', {})


def schedule(request, animal_id):
    return render(request, 'animals/schedule.html', {})