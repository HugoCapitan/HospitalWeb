from django.contrib import admin
from .models import Appointment, AppointmentKind

admin.site.register(Appointment)
admin.site.register(AppointmentKind)
