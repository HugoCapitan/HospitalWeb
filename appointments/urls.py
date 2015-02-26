from django.conf.urls import patterns, url
from .views import AppointmentDetailView_Patient, AppointmentKindListView, AppointmentKindDetailView, AppointmentAddPatientView

urlpatterns = patterns('',
	url(r'^citas/tipos/$', AppointmentKindListView.as_view(), name='appointmentkindlistview'),
    url(r'^citas/tipos/?(?P<kind>[\w\-]+)/$', AppointmentKindListView.as_view(), name='appointmentkindlistview'),
	url(r'^citas/(?P<slug>[\w\-\W]+)/$', AppointmentKindDetailView.as_view(), name='appointmentkindlistview'),
    url(r'^pacientes/cita/(?P<slug>[\w\W]+)/$', AppointmentDetailView_Patient.as_view(), name='appointment_detail'),
    url(r'^pacientes/nueva/$', AppointmentAddPatientView.as_view(), name="appointment_new")
)