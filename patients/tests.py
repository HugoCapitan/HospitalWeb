from django.test import TestCase
from .models import Patient
from django.contrib.auth.models import User

class LogicTest(TestCase):

	# tests de logica
	def setUp(self):
		# se da de alta un usuario y un paciente bien
		test_pat_user = User.objects.create(username='usertest', first_name='Tests', last_name='User', email='user@test.com')
		test_pat = Patient.objects.create(user=test_pat_user, curp='sajfskbfaksdf38233', birth='1999-12-12', phone='+525523870166')

	# def test_existe_(self):
	# 	res = test_pat_user.
	# 	res = self.client.get('/artists/%d/' % self.artist.id)
	# 	self.assertEqual(res.status_code, 200)
	# 	self.assertTrue('AC/DC' in res.content)

	# def test_usuario_logeado(self):
	# 	res = self.client.get('/tracks/%s/' % self.track.title)
	# 	self.assertEqual(res.status_code, 302)

	# def test_no_existe_vista(self):
	# 	id_viejo = self.artist.id
	# 	self.artist.delete()
	# 	res = self.client.get('/artists/%d/' % id_viejo)
	# 	self.assertEqual(res.status_code, 404)
