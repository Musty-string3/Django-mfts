from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class DetailView(generic.DetailView):
    template_name = "detail.html"