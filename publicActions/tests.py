from django.test import TestCase
from .models import Announcement

class LogicTest(TestCase):

	# tests de logica
	def setUp(self):
		# se da de alta un usuario y un paciente bien
		test_ann_user = User.objects.create(username='usertest', first_name='Tests', last_name='User', email='user@test.com')
		test_ann = Announcement.objects.create(title='Testing', content='sajfskbfaksdf38233sd fsd fg sdf sd fs', image='eSfafem/asfdsa')
