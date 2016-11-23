from django.shortcuts import render

from .models import Mission
# Create your views here.


def mission_screen(request, mission_id):
	try:
		mission = Mission.objects.get(pk=mission_id)
	except Mission.DoesNotExist:
		mission = Mission()
		return render(request, 'storymanager/mission_screen.html', {'mission' : mission})
	return render(request, 'storymanager/mission_screen.html', {'mission' : mission})
	