from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .forms import UserForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        pass