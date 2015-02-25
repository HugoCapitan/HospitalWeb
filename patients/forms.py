from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Patient


class PatientCreationForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ('curp', 'birth', 'phone')


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
