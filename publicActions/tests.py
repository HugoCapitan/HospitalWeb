from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Announcement
from django.utils.text import slugify

class WorkTets(TestCase):

	def setUp(self):
		self.test_user = User.objects.create_user(username= 'testing', password = '123')

	def test_add_adress(self):
			title = "Alfredo MVP"
			content = "Contenido Contenido Contenido Contenido Contenido Contenido Contenido Contenido Contenido Contenido Contenido " 
			date = '12/12/12'
			image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')