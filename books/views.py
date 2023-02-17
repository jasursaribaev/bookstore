from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'books/home.html'

class AboutView(TemplateView):
    template_name = 'books/about.html'

class ContactView(TemplateView):
    template_name = 'books/contact.html'
