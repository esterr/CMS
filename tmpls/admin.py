from django.contrib import admin
from django import forms
import cms.easygui as eg
from django.db import models

from tmpls.models import Template

class templateAdmin(admin.ModelAdmin):
	fields = ['typeid', 'name', 'isPublish', 'ispublic']
	search_fields = ['name']
	list_display = ('name', 'typeid', 'isPublish', 'ispublic')
	# license_file = FieldFile(blank=True, upload_to='license')
	# self.fields = (
 #        forms.TextField(field_name='title', length=30, maxlength=100, is_required=True),
 #    )
	def save_model(self, request, form, formset, change):
		eg.msgbox(change, title="simple gui")
		# self.license_file.save("aaa", "{% block title %}")

# class ArticleAdmin(models.Model):
# 	eg.msgbox("aaaa", title="aa")
# 	def save_model(self, request, form, formset, change):
# 		eg.msgbox(form, title="simple gui")
# 		FieldFile.save("aaa", "{% block title %}")

admin.site.register(Template, templateAdmin)

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