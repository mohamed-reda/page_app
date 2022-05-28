from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')
# pages/views.py

from django.views.generic import TemplateView


# the main page
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
