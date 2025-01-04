from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Notice

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "password1"]

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

class NoticeForm(forms.ModelForm):
    schedule = forms.DateTimeField(
        widget = forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "class": "form-control"
        })
    )
    class Meta:
        model = Notice
        fields = ["title", "type", "schedule", "description", "location", "organization"]
