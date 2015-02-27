from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from publicActions.models import Announcement
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor

import datetime

class IndexView(ListView):
	template_name = 'index.html'
	model = Announcement


class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'login.html'
	success_url = '/perfil/'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(self.request, form.user_cache)
		
		return super(LoginView, self).form_valid(form)

	
class ProfileView(TemplateView):
	template_name = 'profile.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProfileView, self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)

		if self.request.user.is_authenticated():
			kind = self.get_user_kind()
			if kind == 'paciente':
				context.update({'us_kind': self.get_user_kind(), 'citas': self.get_citas()})
				return context
			elif kind == 'doctor':
				context.update({'us_kind': self.get_user_kind(), 'citas': self.get_citas()})
				return context
		else:
			return 'hola'

		
	def get_user_id(self):
		user = self.request.user;
		user_id = user.id;
		return user_id

	def get_user_kind(self):
		try:	
			patient = Patient.objects.get(user = self.get_user_id())
			return 'paciente'
		except Patient.DoesNotExist:
			return 'doctor'

	def get_patient(self):
		return Patient.objects.get(user = self.get_user_id())

	def get_doctor(self):
		return Doctor.objects.get(user = self.get_user_id()) 

	def get_citas(self):
		kind = self.get_user_kind()
		if kind == 'paciente':
			patient = self.get_patient()
			try:
				citas = Appointment.objects.filter(date__gt=datetime.datetime.now(), patient=patient)
			except Appointment.DoesNotExist:
				citas = None
			return citas
		elif kind == 'doctor':
			doctor = self.get_doctor()
			try:
				citas = Appointment.objects.filter(date__gt=datetime.datetime.now(), doctor=doctor)
			except Appointment.DoesNotExist:
				citas = None
			return citas

		


