from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'auth-input', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'auth-input', 'type':'password', 'align':'center'}),
    )
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'auth-input'}),
            'first_name': forms.TextInput(attrs={'class': 'auth-input'}),
            'last_name': forms.TextInput(attrs={'class': 'auth-input'}),
            'email': forms.TextInput(attrs={'class': 'auth-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'auth-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'auth-input'}),
        }
