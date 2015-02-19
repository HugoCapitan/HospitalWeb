from django.db import models

from doctors.models import Doctor
from patients.models import Patient


class Diagnostic(models.Model):

	primary_content = models.TextField(blank=False)
	treatment = models.TextField()
	results = models.TextField()
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	date = models.DateField(auto_now=True, blank=False)

	# PENDIENTE:
	# primary key (paciente_diagnostico, medico_diagnostico, fecha_diagnostico)

	class Meta:
		verbose_name = "diagnostic"
		verbose_name_plural = "diagnostics"

	def __str__(self):
		pass
	

class Message(models.Model):

	content = models.TextField(blank=False)
	date_time = models.DateTimeField(auto_now=True)
	doctor = models.ForeignKey(Doctor)
	patient = models.ForeignKey(Patient)

	class Meta:
		verbose_name = "message"
		verbose_name_plural = "messages"

	def __str__(self):
		pass    