from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    f = UserCreationForm()
    return render(request, "registration/register.html", {'form': f})