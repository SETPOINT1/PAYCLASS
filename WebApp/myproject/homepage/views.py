from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'homepage/home.html')  # หน้าแรก

def login_view(request):
    return render(request, 'homepage/login.html')  # หน้า Login

def about_us_view(request):
    return render(request, 'homepage/about_us.html') # หน้า About us

def register_view(request):
    return render(request, 'homepage/register.html') # หน้า About us