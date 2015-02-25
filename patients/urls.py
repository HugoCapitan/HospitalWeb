from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import ProfileView, LoginView, FillingView, SignupView


urlpatterns = patterns('',
	url(r'^pacientes/signup/$', SignupView.as_view(), name='signup'),
	url(r'^pacientes/signup/end/$', FillingView.as_view(), name='filling'),
	url(r'^pacientes/perfil/$', ProfileView.as_view(), name='profile'),
	url(r'^pacientes/login/$', LoginView.as_view(), name='login'),
	url(r'^accounts/profile/$', RedirectView.as_view(url='../../patients/profile'))

)