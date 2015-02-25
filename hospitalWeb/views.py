from django.shortcuts import render
from django.views.generic import ListView
from publicActions.models import Announcement


class IndexView(ListView):
	template_name = 'index.html'
	model = Announcement