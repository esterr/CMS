from django.db import models 

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
