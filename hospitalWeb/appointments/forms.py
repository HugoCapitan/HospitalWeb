from django import forms

from .models import Appointment

from datetimewidget.widgets import DateTimeWidget

class AppointmentCreationForm(forms.ModelForm):

	date = forms.DateTimeField(widget=DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = False, bootstrap_version=3))

	class Meta:
		model = Appointment
		fields = ('kind', 'doctor', 'comment', 'date')
		widgets = {
			#Use localization and bootstrap 3
			'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = False, bootstrap_version=3)
		}