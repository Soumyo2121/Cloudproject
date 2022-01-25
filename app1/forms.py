from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		# password = forms.CharField(widget=forms.PasswordInput())
		model = User
		fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']

		