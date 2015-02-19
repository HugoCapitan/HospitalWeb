from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .forms import UserCreationEmailForm


def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()
		authentication_data = form.get_authentication_data()
		return HttpResponse('Bien')

	return render(request, 'signup.html', {'form': form})