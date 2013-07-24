from django.contrib import admin
from django.contrib import messages
from django.db import models

from tmpls_types.models import Type

class TemplateTypeAdmin(admin.ModelAdmin):
	fieldsets = [
        (None, {'fields': ['name', 'description']}),
    ]
	list_display = ('id', 'name', 'description')
	# list_filter = ['name']
	search_fields = ['name']


admin.site.register(Type, TemplateTypeAdmin)
		