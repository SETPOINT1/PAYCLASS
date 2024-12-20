from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('', views.home_view, name='home'),  # หน้าแรก
    path('login/', views.login_view, name='login'),  # หน้า Login
    path('AboutUs/', views.about_us_view, name='AboutUs'),  # หน้า About Us
    path('register/', views.register_view, name='register'),  # หน้า Register
    path('logout/', views.logout_view, name='logout'),  # หน้า Logout
    path('admin/', admin.site.urls),  # เส้นทาง Admin Panel
]
