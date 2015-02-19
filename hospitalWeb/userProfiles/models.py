from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	avatar = models.ImageField(upload_to='avatars')
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username