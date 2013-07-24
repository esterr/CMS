from django.contrib import admin
from django import forms
import cms.easygui as eg
from django.db import models

from tmpls_types.models import Type
from tmpls.models import Template
		# self.license_file.save("aaa", "{% block title %}")

# class ArticleAdmin(models.Model):
# 	eg.msgbox("aaaa", title="aa")
# 	def save_model(self, request, form, formset, change):
# 		eg.msgbox(form, title="simple gui")
# 		FieldFile.save("aaa", "{% block title %}")

# from django import forms
# class TodoListForm(forms):
#     def __init__(self, request):
#         self.fields = (
#             forms.TextField(field_name='title', length=30, maxlength=100, is_required=True),
#         )
#         self.request = request
    
#     def save(self, new_data):
#     	eg.msgbox("aaaa", title="aa")
#         return TodoList.objects.create_list(new_data['title'], self.request.user)
class TemplateAdmin(admin.ModelAdmin):
	list_display = ('name', 'templateType', 'isPublish', 'isPublic')
	list_filter = ('templateType__name', 'isPublish', 'isPublic')
	search_fields = ['name']
	def save_model(self, request, form, formset, change):
		eg.msgbox(change, title="simple gui")

admin.site.register(Template, TemplateAdmin)
