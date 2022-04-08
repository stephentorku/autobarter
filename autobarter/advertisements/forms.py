from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserDetails
from .models import *

class UserDetailsForm(ModelForm):
	class Meta:
		model = UserDetails
		fields = '__all__'
		exclude = ['user']