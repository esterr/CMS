from django.db import models
from django.contrib.auth.models import User
import cms.easygui as eg

from tmpls_types.models import Type

class Template(models.Model):
	templateType = models.ForeignKey(Type)
	name = models.CharField(max_length=300)
	content = models.CharField(max_length=500)
	isPublish = models.BooleanField()
	isPublic = models.BooleanField()
	users = models.ManyToManyField(User, null=True)
	
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

	def display_template(self):
		return '<a harf=%s>%s</a>' % ('template/'+self.name.replace(" ","_").lower() , 'template/'+self.name.replace(" ","_").lower())
	display_template.allow_tags = True

# class TemplatesUser(models.Model):
# 	template = models.ForeignKey(Template)
# 	user = models.ForeignKey(User)

