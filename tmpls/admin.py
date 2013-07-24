from django.contrib import admin
from tmpls.models import Template
from tmpls_types.models import Type

class TemplateAdmin(admin.ModelAdmin):
	list_display = ('name', 'templateType', 'isPublish', 'isPublic')
	list_filter = ('templateType__name', 'isPublish', 'isPublic')
	search_fields = ['name']

admin.site.register(Template, TemplateAdmin)

