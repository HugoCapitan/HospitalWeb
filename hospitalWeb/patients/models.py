from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User


class Patient(models.Model):

	user = models.OneToOneField(User)
	curp = models.CharField(max_length=18, blank=False)
	birth = models.DateField(auto_now=False, auto_now_add=False, blank=False)
	phone = PhoneNumberField(blank=False)


	class Meta:
		verbose_name = "Patient"
		verbose_name_plural = "Patients"

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)