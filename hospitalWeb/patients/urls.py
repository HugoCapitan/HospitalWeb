from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^signup/', 'patients.views.signup', name='signup'),
	url(r'^data_filling/', 'patients.views.data_filling', name='data_filling'),

)