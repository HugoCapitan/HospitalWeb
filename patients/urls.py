from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import FillingView, SignupView


urlpatterns = patterns('',
	url(r'^pacientes/signup/$', SignupView.as_view(), name='signup'),
	url(r'^pacientes/signup/end/$', FillingView.as_view(), name='filling'),

)