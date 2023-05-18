from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crud.models import Student

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

@login_required
#Home
# Fetching all data 
def home(request):
    student = Student.objects.all()
    context = {
        'Student' : student
    }
    return render(request, "home.html", context)

#create [C]
def Create(request):
    if request.method == 'POST':
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        
        student = Student()
        
        student.name = name
        student.email = email
        student.address = address
        
        student.save()
    else:
        print("post method not working..")
    return redirect('/home')

# Delete [D]
def Delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/home')
