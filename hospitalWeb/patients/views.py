from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import UserCreationEmailForm, PatientDataFillingForm
from .models import Patient

from appointments.models import Appointment

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

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
			return render(request, 'first_welcome.html', {'data': f_data})

	return render(request, 'signup.html', {'form': form})



@login_required
def filling(request):
	form = PatientDataFillingForm(request.POST or None)

	if form.is_valid():
		user = request.user
		pat = form.save(commit=False)
		pat.user = user
		pat.save()
		return render(request, 'data_filling_completed.html', {'user': user})

	return render(request, 'filling.html', {'form': form})



def signin(request):

	form = AuthenticationForm(request.POST or None)
	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'login.html', {'form': form})

import datetime

class ProfileView(TemplateView):
	template_name = 'profile.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)

		if self.request.user.is_authenticated():
			context.update({'patient': self.get_patient(), 'citas': self.get_citas()})

		return context

	def get_patient(self):
		user = self.request.user;
		user_id = user.id;
		patient = Patient.objects.get(user = user_id)
		return patient

	def get_citas(self):
		user = self.request.user;
		user_id = user.id;
		patient = Patient.objects.get(user = user_id)
		try:
			citas = Appointment.objects.filter(date__gt=datetime.datetime.now())
		except Appointment.DoesNotExist:
			citas = None
		return citas
