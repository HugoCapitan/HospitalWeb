from django.conf.urls import patterns, url
from .views import AppointmentDetailView_Patient, AppointmentKindListView

urlpatterns = patterns('',
	url(r'^appointments/kinds/$', AppointmentKindListView.as_view(), name='appointmentkindlistview'),
    url(r'^appointments/kinds/(?P<kind>[\w\-]+)/$', AppointmentKindListView.as_view(), name='appointmentkindlistview'),
	url(r'^appointments/(?P<kind>[\w\-]+)/$', AppointmentKindDetailView.as_view(), name='appointmentkindlistview'),
    url(r'^patients/appointment/(?P<slug>[\w\W]+)/$', AppointmentDetailView_Patient.as_view(), name='appointment_detail'),
)