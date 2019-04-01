from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('app.index')
        else:
            return render(request, "register/register.html", {"form": f})
    else:
        f = UserCreationForm()
        return render(request, "register/register.html", {"form": f})
