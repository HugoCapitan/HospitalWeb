from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email')


	def clean_email(self):
		email = self.cleaned_data.get('email')
	 	try:
	 		User.objects.get(email = email)
	 		raise forms.ValidationError('Email Repetido')
	 	except User.DoesNotExist:
	 		return email


	def get_authentication_data(self):
	 	authentication_data = {'username': self.cleaned_data.get('username'), 'email': self.cleaned_data.get('email'), 'password': self.cleaned_data.get('password1')}
	 	return authentication_data