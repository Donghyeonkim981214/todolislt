from django.shortcuts import render
from django.views.generic import TemplateView
from . import mixins
# Create your views here.

class HomeView(mixins.LoggedOutOnlyView, TemplateView):
    template_name = "home.html"
