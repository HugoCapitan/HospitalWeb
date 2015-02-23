from django.db import models

from doctors.models import Doctor
from patients.models import Patient



class AppointmentKind(models.Model):
	kind = models.CharField(max_length=50, blank=False, primary_key=True)
	duration = models.PositiveIntegerField(blank=False)
	doctors = models.ManyToManyField(Doctor)

	class Meta:
		verbose_name = "AppointmentKind"
		verbose_name_plural = "AppointmentKinds"

	def __str__(self):
		return self.kind

		
class Appointment(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	comment = models.TextField(blank= True)
	kind = models.ForeignKey(AppointmentKind)
	confirmed = models.BooleanField(default=False)
	primaryKey = models.CharField(max_length=255, primary_key=True, editable=False)
	slug = models.CharField(max_length=255, editable=False,unique=True)

	def save(self, *args, **kwargs):
		doctor = self.doctor.medical_identification_card
		patient = self.patient.curp

		date = self.date.date()
		time = self.date.time()

		day = self.date.day
		month = self.date.month
		year = self.date.year
		hour = self.date.hour
		minute = self.date.minute

		self.primaryKey = 'Doctor: %s, Paciente: %s, Dia: %s, Hora: %s' % (doctor, patient, date, time)
		self.slug = 'doc-%s-pat-%s-day-%s-month-%s-year-%s-hour-%s-minute-%s' % (doctor, patient, day, month, year, hour, minute)

		super(Appointment, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Appointment"
		verbose_name_plural = "Appointments"

	def __str__(self):
		return 'Doctor: %s, Paciente: %s, Dia: %s, Horario: %s' % (self.doctor, self.patient, self.date.date(), self.date.time())
