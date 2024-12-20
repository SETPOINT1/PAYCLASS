from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'line', 'password1', 'password2', 'phone_number']

class LoginForm(AuthenticationForm):
    pass

 # กำหนด Widget สำหรับฟิลด์ line
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['line'].widget = forms.TextInput(attrs={'placeholder': 'Enter your Line ID'})