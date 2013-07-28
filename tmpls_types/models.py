from django.db import models 

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300, null=True)
	layout = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.name
		
	def __str__(self):
		return self.name
