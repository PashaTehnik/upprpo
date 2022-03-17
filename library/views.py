from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template("library/index.html")
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


# def index(request):
#     return render(request, 'library\index.html')