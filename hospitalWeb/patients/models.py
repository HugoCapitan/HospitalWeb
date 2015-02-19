from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from userProfiles.models import UserProfile


class Patient(models.Model):

	profile = models.OneToOneField(UserProfile)
	birth = models.DateField(auto_now=False, auto_now_add=False, blank=False)
	phone = PhoneNumberField(blank=False)


	class Meta:
		verbose_name = "Patient"
		verbose_name_plural = "Patients"

	def __str__(self):
		return self.profile.user.first_name