from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

# Create your views here.
def home(request):
    template= loader.get_template('home.html')
    context ={
        'company_name':'goodies'
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