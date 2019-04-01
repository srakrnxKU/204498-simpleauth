from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    f = UserCreationForm()
    return render(request, "register/register.html", {"form": f})
