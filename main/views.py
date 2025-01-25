from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"


# def index(request):
#     return render(request, "main/index.html")


class AboutView(TemplateView):
    template_name = "main/about_us.html"


# def about(request):
#     return render(request, "main/about_us.html")
