from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import UppyUserCredentials

# Create your views here.


def profile(request, user):
    context = {'user': user, 'obj': UppyUserCredentials.objects.first()}
    return render(request, 'auth/profile.html', context=context)

def signup(request):
    return render(request, 'auth/signup.html')


def login_user(request):
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def forgetPass(request):
    return render(request, 'auth/forget-password.html')


def resetPass(request):
    return render(request, 'auth/reset-password.html')

