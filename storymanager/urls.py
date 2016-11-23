from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^mission_(?P<mission_id>[0-9]+)/$', views.mission_screen, name='mission_screen'),
	
]