from django.shortcuts import render

from .models import Mission
# Create your views here.

def home_screen(request):
	return render(request, 'storymanager/home_screen.html')

def mission_screen(request, mission_id):
	try:
		mission = Mission.objects.get(pk=mission_id)
	except Mission.DoesNotExist:
		mission = Mission()
		return render(request, 'storymanager/mission_screen.html', {'mission' : mission})
	return render(request, 'storymanager/mission_screen.html', {'mission' : mission})
	
def repository_screen(request):
	return render(request, 'storymanager/repository_screen.html')

def scene_screen(request, mission_id, scene_id):
	return render(request, 'storymanager/scene_screen.html')
