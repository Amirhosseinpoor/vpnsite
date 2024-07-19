from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


class BlogView(TemplateView):
    template_name = 'blog.html'
# Create your views here.
