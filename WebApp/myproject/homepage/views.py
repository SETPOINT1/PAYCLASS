from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'homepage/home.html')  # หน้าแรก

def login_view(request):
    return render(request, 'homepage/login.html')  # หน้า Login