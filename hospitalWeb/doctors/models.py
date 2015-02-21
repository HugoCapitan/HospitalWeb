from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User


class Doctor(models.Model):

	user = models.OneToOneField(User)
	medical_identification_card = models.CharField(max_length=20, blank=False, unique=True)
	egress = models.CharField(max_length=50, blank=False)
	specialism = models.CharField(max_length=50, blank=False)
	phone = PhoneNumberField(blank=False)
	schedule = models.TextField(blank=False)
	avatar = models.ImageField(upload_to='Doctors')

	class Meta:
		verbose_name = "Doctor"
		verbose_name_plural = "Doctors"

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)