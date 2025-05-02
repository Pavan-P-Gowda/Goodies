from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .models import Car

# Create your views here.
def home(request):
    template= loader.get_template('home.html')
    context ={
        'cars': Car.objects.all()
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template= loader.get_template('about.html')
    context={

    }
    return HttpResponse(template.render(context,request))

def contact(request):
    template= loader.get_template('contact.html')
    context={

    }
    return HttpResponse(template.render(context,request))