from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^home/$', views.home_screen, name='home'),
	url(r'^mission_(?P<mission_id>[0-9]+)/$', views.mission_screen, name='mission_screen'),
	url(r'^mission_(?P<mission_id>[0-9]+)/scene_(?P<scene_id>[0-9]+)/$', views.scene_screen, name="scene_screen"),
	url(r'^repo/$', views.repository_screen, name="repository_screen"),
]