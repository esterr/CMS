from django.contrib import admin
from tmpls.models import Template
from tmpls_types.models import Type

class TemplateAdmin(admin.ModelAdmin):
	list_display = ('name', 'templateType', 'isPublish', 'isPublic')
	list_filter = ['templateType', 'isPublish', 'isPublic']

admin.site.register(Template, TemplateAdmin)

