from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Appointment, AppointmentKind
from .forms import AppointmentCreationForm


class AppointmentDetailView_Patient(DetailView):
	model = Appointment
	template_name = 'appointment_patient_detail.html'


def AppointmentAdd_Patient(request):
	form = AppointmentCreationForm

	if form.is_valid():
		appoint = form.save(commit=False)
		appoint.patient = self.get_patient()
		appoint.save()

	def get_patient(self):
		user = self.request.user;
		user_id = user.id;
		patient = Patient.objects.get(user = user_id)
		return patient


class AppointmentKindListView(ListView):
	model = AppointmentKind
	template_name = "appointmentkind_list.html"
	paginate_by = 10

	def get_queryset(self):
		if self.kwargs.get('kind'):
			queryset = self.model.objects.filter(kind__contains=self.kwargs['kind'])
		else:
			queryset = super(AppointmentKindListView, self).get_queryset()

		return queryset

class AppointmentKindDetailView(DetailView):
    model = AppointmentKindDetailView
    template_name = "appointmentkind_detail.html"
