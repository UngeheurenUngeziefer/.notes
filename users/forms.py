from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=200, help_text='')
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(max_length=200, help_text='')
    password2 = forms.CharField(max_length=200, help_text='')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
