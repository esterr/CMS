from django.contrib import admin
from django.core.files import File
import cms.easygui as eg
from django.db import models
from django import forms
from django.conf import settings
import os

from tmpls_types.models import Type
from tmpls.models import Template
import cms.globals as glb

class TemplateModelForm( forms.ModelForm ):
	
	content = forms.CharField(widget=forms.Textarea )

	class Meta:
		model = Template

	def __init__(self, *args, **kwargs):
		super(TemplateModelForm, self).__init__(*args, **kwargs)

		if self.instance.name == "":
			fileName = "init"
		else:
			fileName = self.initial['name'].replace(" ", "_").lower()

		myFile = File(open(glb.fileRoot + fileName + '.html','r'))
		cont = myFile.read()
		myFile.close()
		cont = cont[cont.index("{% block",cont.index(glb.endTitleBlock) + len(glb.endTitleBlock)):]
		self.initial['content'] = cont

class TemplateAdmin(admin.ModelAdmin):

	form = TemplateModelForm

	list_display = ('name', 'templateType', 'isPublish', 'isPublic','display_template')
	list_filter = ('templateType__name', 'isPublish', 'isPublic')
	search_fields = ['name']

	def save_model(self, request, form, formset, change):
		super(TemplateAdmin, self).save_model(request, form, formset, change)

		nameTpl = form.name.replace(" ", "_").lower()
		extend = glb.extendBlock + form.templateType.name.lower() + glb.endExtendBlock + "\n" 
		title =  glb.titleBlock + form.name + glb.endTitleBlock + "\n"
		content = extend + title + form.content
		myFile = File(open(glb.fileRoot + nameTpl +'.html','w'))
		myFile.write(content)
		myFile.close()

	def delete_model(self, request, obj):
		fileName = obj.name.replace(" ", "_").lower()
		path = glb.fileRoot + fileName + '.html'
		os.remove(path)
		super(TemplateAdmin,self).delete_model(request, obj)

admin.site.register(Template, TemplateAdmin)