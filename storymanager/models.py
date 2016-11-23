from django.db import models


# Create your models here.

class Story(models.Model):
	name = models.CharField(max_length=1000)
	source_book = models.CharField(max_length = 500)
	date_created = models.DateTimeField(True)
	def __str__(self):
		return self.name + ", created on:" + date_created

class Mission(models.Model):
	story = models.ForeignKey(Story, on_delete = models.CASCADE)
	mission_name = models.CharField(max_length = 1000)
	date_created = models.DateTimeField(True)
	flowchart_json = models.TextField()

	def __str__(self):
		return self.story.name + "\\" + self.mission_name + ", created on: " + date_created