from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import ProfileView, LoginView


urlpatterns = patterns('',
	url(r'^patients/signup/', 'patients.views.signup', name='signup'),
	url(r'^patients/filling/', 'patients.views.filling', name='filling'),
	url(r'^patients/profile/$', ProfileView.as_view(), name='profile'),
	url(r'^patients/login/$', LoginView.as_view(), name='login'),
	url(r'^accounts/profile/$', RedirectView.as_view(url='../../patients/profile'))

)