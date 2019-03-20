from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("This is the login page")


def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass
