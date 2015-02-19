from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .forms import UserCreationEmailForm, PatientDataFillingForm


def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()
		authentication_data = form.get_authentication_data()

		#Logear al usuario

		return HttpResponse('Felicidades Completaste tu registro <a href="localhost:8000/data_filling">Completa tu Registro</a>')

	return render(request, 'signup.html', {'form': form})

def data_filling(request):
	form = PatientDataFillingForm(request.POST or None)

	if form.is_valid():
		form.save()
		return HttpResponse('Bien')

	return render(request, 'data_filling.html', {'form': form})