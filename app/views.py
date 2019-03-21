from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from . import random_quotes


def index(request):
    if request.user.is_authenticated:
        quote = random_quotes.random_quote()
        print(quote)
        return render(request, "login/home.html", quote)
    else:
        return render(request, "login/login.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect("app.index")


def logout_page(request):
    logout(request)
    return redirect("app.index")
