from django.test import TestCase
from .models import Doctor

class LogicTest(TestCase):

	# tests de logica
	def setUp(self):
		# se da de alta un usuario y un paciente bien
		test_doc_user = User.objects.create(username='usertest', first_name='Tests', last_name='User', email='user@test.com')
		test_doc = Doctor.objects.create(user=test_doc_user, medical_identification_card='sajfskbfaksdf3823333', egress='UNAM', specialism='Odontologia', phone='+525523870166', schedule='hasifnasfnas fjsa fsahfjaskd fksa')
