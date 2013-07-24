from django.shortcuts import render

from tmpls_types.models import Type

def index(request):
    listTypeTemplate = Type.objects.all()
    context = {'listTypeTemplate': listTypeTemplate}
    return render(request, 'tmpls_types/indexBlocks.html', context)

# def shoes(request):
# 	return render(request, 'shoes.html')