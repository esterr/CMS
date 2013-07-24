from django.db import models
from django.contrib.auth.models import User
from tmpls_types.models import Type

class Template(models.Model):
	templateType = models.ForeignKey(Type)
	name = models.CharField(max_length=300)
	isPublish = models.BooleanField()
	isPublic = models.BooleanField()
	users = models.ManyToManyField(User, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

# class TemplatesUser(models.Model):
# 	template = models.ForeignKey(Template)
# 	user = models.ForeignKey(User)

