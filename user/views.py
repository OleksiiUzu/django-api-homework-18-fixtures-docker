from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        user_data = [username, useremail]
        return render(request, 'user/user.html', {'data': user_data})
    else:
        return redirect('/user/login')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/user/login')
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'user/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('/user/login')


def user_register(request):
    if request.method == 'POST':
        new_user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password'],
                                            email=request.POST['email'],
                                            )
        new_user.save()
        return redirect('/user/login')
    return render(request, 'user/register.html', {})


def user_history(request):
    return render(request, 'user/history.html', {})
