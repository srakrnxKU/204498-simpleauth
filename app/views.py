from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def index(request):
    return render(request, "login/login.html")


def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    print("{} {}".format(username, password))
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Yay")
    else:
        return redirect("index")
