from django.contrib import admin
from django.contrib import messages
from django.db import models
from django import forms

from tmpls_types.models import Type

class TemplateTypeModelForm( forms.ModelForm ):

	# get layout file contet into "layout" field
	def __init__(self, *args, **kwargs):
		super(TemplateTypeModelForm, self).__init__(*args, **kwargs)

		fileName = self.instance.name.replace(" ", "_").lower()
		try:
			f = open("tmpls_types\\templates\\" + self.instance.name + ".html", "r")
			content = f.read() #Get layout file content
			f.close()
		except IOError:
			content = ""
			
		self.initial['layout'] = content

	# layout field as textarea
	layout = forms.CharField( widget = forms.Textarea(attrs = {'size': '200', 'cols':80}) )
	class Meta:
		model = Type


class TemplateTypeAdmin(admin.ModelAdmin):
	form = TemplateTypeModelForm
	fieldsets = [
        (None, {'fields': ['name', 'description', 'layout']}),
    ]
	list_display = ('id', 'name', 'description')
	search_fields = ['name']

	# save the layout field into file
	def save_model(self, request, form, formset, change):
		super(TemplateTypeAdmin, self).save_model(request, form, formset, change)

		fileName = form.name.replace(" ", "_").lower()
		f = open("tmpls_types\\templates\\" + fileName + ".html", "w")
		try:
			f.write(form.layout) #Create the layout file
		finally:
			f.close()

admin.site.register(Type, TemplateTypeAdmin)
		