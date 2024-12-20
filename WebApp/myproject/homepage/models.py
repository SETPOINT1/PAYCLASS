from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # เพิ่มฟิลด์ที่อยู่
    line = models.CharField(max_length=50, blank=True, null=True)  # เปลี่ยนเป็น CharField
