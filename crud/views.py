from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

# def register(request):
#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
        
#         if f.is_valid():
#             f.save()
            
#             return redirect('index')
#     else:
#         f = UserCreationForm()
            
#     return render(request, 'registration/register.html', {'form': f})

#Register
def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('index')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})
