from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    profile_pic = forms.ImageField(required=False)  # Optional
    github_link = forms.URLField(required=False)  # Optional

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'profile_pic', 
            'github_link', 
            'password1', 
            'password2'
        ]