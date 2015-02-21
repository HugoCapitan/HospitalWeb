from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import UserCreationEmailForm, PatientDataFillingForm


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
		form.save()
		return render(request, 'profile.html', {'patient': request.patient})

	return render(request, 'filling.html', {'form': form})