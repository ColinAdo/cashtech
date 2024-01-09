from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'Placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']