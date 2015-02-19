from django.db import models

from doctors.models import Doctor
from patients.models import Patient



class AppointmentKind(models.Model):
	kind = models.CharField(max_length=50, blank=False)
	duration = models.PositiveIntegerField(blank=False)
	doctors = models.ManyToManyField(Doctor)

	# PENDIENTE:
	# primary key(nombre_tipocita, medico_tipocita)

	class Meta:
		verbose_name = "AppointmentKind"
		verbose_name_plural = "AppointmentKinds"

	def __str__(self):
		return self.kind

		
class Appointment(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	comment = models.TextField()
	kind = models.ForeignKey(AppointmentKind)
	confirmed = models.BooleanField(default=False)

	# PENDIENTE:
	# primary key (fecha_cita, paciente_cita, medico_cita)

	class Meta:
		verbose_name = "Appointment"
		verbose_name_plural = "Appointments"

	def __str__(self):
		return 'Doctor: %s, Paciente: %s, Horario: %s' % (self.doctor, self.patient, self.date)


