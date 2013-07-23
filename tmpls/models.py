from django.db import models
from tmpls_types.models import Type
from users.models import User

class Template(models.Model):
	typeid = models.ForeignKey(Type)
	name = models.CharField(max_length=300)
	isPublish = models.BooleanField()
	ispublic = models.BooleanField()

class TemplatesUsers(models.Model):
	templateid = models.ForeignKey(Template)
	userid = models.ForeignKey(User)

