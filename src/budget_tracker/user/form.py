from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','date_of_birth', 'password1', 'password2')