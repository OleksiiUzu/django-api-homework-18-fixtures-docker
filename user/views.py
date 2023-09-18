from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'user/user.html', {})


def user_login(request):
    return render(request, 'user/login.html', {})


def user_logout(request):
    return render(request, 'user/logout.html', {})


def user_register(request):
    return render(request, 'user/register.html', {})


def user_history(request):
    return render(request, 'user/history.html', {})
