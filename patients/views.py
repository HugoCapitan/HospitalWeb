from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from .forms import PatientCreationForm
from .models import Patient

from hospitalWeb.forms import UserCreationCompleteForm
from appointments.models import Appointment

import datetime


class FillingView(FormView):
	form_class = PatientCreationForm
	template_name = 'filling.html'
	success_url = '/pacientes/perfil/'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = request.user
			instance = form.save(commit=False)
			instance.user = user
			instance.save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)



class SignupView(FormView):
	form_class = UserCreationCompleteForm
	template_name = 'signup.html'
	success_url = '/pacientes/signup/end/'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			authentication_data = form.get_authentication_data()
			user = authenticate(username = authentication_data['username'], password = authentication_data['password'])
			login(request, user)
			if request.user.is_authenticated():
				username = request.user.username
				email = request.user.email
				f_data = {
					'username': username,
					'email': email
				}
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

