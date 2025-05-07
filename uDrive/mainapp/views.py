from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .models import Car
from django.views.generic import DetailView

# Create your views here.
def home(request):
    template= loader.get_template('home.html')
    context ={
        'cars': Car.objects.all(),
        'current_page' : 'home'
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template= loader.get_template('about.html')
    context={
        'current_page' : 'about'

    }
    return HttpResponse(template.render(context,request))

def contact(request):
    template= loader.get_template('contact.html')
    context={
        'current_page' : 'contact'
    }
    return HttpResponse(template.render(context,request))

class CarDetails(DetailView):
    template_name = 'car_detail.html'
    model = Car
