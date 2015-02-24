from django.db import models

from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


class Diagnostic(models.Model):

	primary_content = models.TextField(blank=False)
	treatment = models.TextField(blank=True)
	results = models.TextField(blank=True)
	appointment = models.ForeignKey(Appointment)
	date = models.DateField(auto_now=True, blank=False)
	slug = models.CharField(max_length=255, editable=False)
	primaryKey = models.CharField(max_length=50, primary_key=True, editable=False)

	def save(self, *args, **kwargs):
		self.primaryKey = 'Doctor: %s, Paciente: %s, Horario: %s' % (self.doctor.medical_identification_card, self.patient.curp, self.date)
		self.slug = '%s-%s-%s' % (self.doctor.medical_identification_card, self.patient.curp, self.date)
		super(Diagnostic, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "diagnostic"
		verbose_name_plural = "diagnostics"

	def __str__(self):
		return 'Doctor: %s, Paciente: %s, Horario: %s' % (self.doctor, self.patient, self.date)
	

class Message(models.Model):

	content = models.TextField(blank=False)
	date_time = models.DateTimeField(auto_now=True)
	doctor = models.ForeignKey(Doctor)
	patient = models.ForeignKey(Patient)

	class Meta:
		verbose_name = "message"
		verbose_name_plural = "messages"

	def __str__(self):
		return 'Doctor: %s, Paciente: %s' % (self.doctor, self.patient)