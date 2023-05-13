from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

#Register
def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully! Please Log In')
            return redirect('index')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})
