from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Doctor(models.Model):
	nombre_medico = models.CharField(max_length=20, blank=False)
	paterno_medico = models.CharField(max_length=20, blank=False)
	materno_medico = models.CharField(max_length=20, blank=False)
	email_medico = models.CharField(max_length=100, blank=False)
	cedula_medico = models.CharField(max_length=20, blank=False)
    egreso_medico = models.CharField(max_length=50, blank=False)
    especialidad_medico = models.CharField(max_length=30, blank=False)
    telefono_medico = models.PhoneNumberField()
    horarios_medico = models.TextField()




    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        pass
    