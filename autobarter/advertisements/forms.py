from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserDetails
from .models import *
from django.forms import ModelForm, TextInput, EmailInput, ImageField

class UserDetailsForm(ModelForm):
	class Meta:
		model = UserDetails
		fields = '__all__'
		exclude = ['user']

		widgets = {
            'first_name': TextInput(attrs={
                'class': "custom-input-rect-form",
                }),
			'last_name': TextInput(attrs={
			'class': "custom-input-rect-form",
                }),
            'email': EmailInput(attrs={
                'class': "custom-input-rect-form", 
                }),
			'username': TextInput(attrs={
			'class': "custom-input-rect-form",
                }),
			'phone_number': TextInput(attrs={
			'class': "custom-input-rect-form",
                }),
        }