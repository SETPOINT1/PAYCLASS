from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # หน้าแรก
    path('login/', views.login_view, name='login'),  # หน้า Login
]

