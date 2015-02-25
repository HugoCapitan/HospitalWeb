from django.shortcuts import render

from django.views.generic import DetailView, ListView, FormView

from django.contrib.auth.decorators import login_required 

from .models import Appointment, AppointmentKind
from .forms import AppointmentCreationForm

from patients.models import Patient

class AppointmentDetailView_Patient(DetailView):
	model = Appointment
	template_name = 'appointment_detail_patient.html'


class AppointmentAddPatientView(FormView):
	form_class = AppointmentCreationForm
	template_name = 'appointment_creation_patient.html'
	success_url = '/patients/profile/'

	def form_valid(self, form):
		patient = self.get_patient()
		appoint = form.save(commit = False)
		appoint.patient = patient
		appoint.save()

		return super(AppointmentAddPatientView, self).form_valid(form)

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
    model = AppointmentKind
    template_name = "appointmentkind_detail.html"
