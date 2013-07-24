from django.contrib import admin
from django.contrib import messages
from django.db import models

from tmpls_types.models import Type

from django import forms
class TemplateTypeModelForm( forms.ModelForm ):
	layout = forms.CharField( widget=forms.Textarea(attrs={'size': '200', 'cols':80}) )
	class Meta:
		model = Type


class TemplateTypeAdmin(admin.ModelAdmin):
	form = TemplateTypeModelForm
	fieldsets = [
        (None, {'fields': ['name', 'description', 'layout']}),
    ]
	list_display = ('id', 'name', 'description')
	# list_filter = ['name']
	search_fields = ['name']

	def save_model(self, request, form, formset, change):
		super(TemplateTypeAdmin, self).save_model(request, form, formset, change)

		fileName = "_".join(form.name.lower().split(" "))
		f = open("tmpls_types\\templates\\" + fileName + ".html", "w+")
		try:
			f.write(form.layout) #Create the layout file
		finally:
			f.close()

admin.site.register(Type, TemplateTypeAdmin)
		