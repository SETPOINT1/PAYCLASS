from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def home_view(request):
    return render(request, 'homepage/home.html')

def about_us_view(request):
    return render(request, 'homepage/about_us.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'homepage/register.html', {'form': form})

def login_view(request):  # ตรงนี้คือส่วนที่แก้ไข
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:  # ตรวจสอบสิทธิ์ของผู้ใช้
                return redirect('/admin/')  # Superuser จะไปหน้า Admin Panel
            else:
                return redirect('home')  # ผู้ใช้ทั่วไปจะไปหน้า Home
    else:
        form = AuthenticationForm()
    return render(request, 'homepage/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
