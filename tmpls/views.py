from django.shortcuts import render

from tmpls.models import Template

def index(request, template_name):
    # listTypeTemplate = Template.objects.get(name = template_name)
    # context = {'listTypeTemplate': listTypeTemplate}
    return render(request, 'tmpls/'+ template_name +'.html')