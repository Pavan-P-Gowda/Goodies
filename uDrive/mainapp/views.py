from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .models import Car
from django.views.generic import DetailView, DeleteView, UpdateView,CreateView

from .forms import CarForm
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

class AddCar(CreateView):
    model = Car
    template_name = "add_car.html"
    form_class = CarForm
    success_url = '/'

class CarEdit(UpdateView):
    model = Car
    context_object_name = 'car'
    template_name = "car_edit.html"
    fields = ['img','price','fuel','transmission']
    success_url = '/'

class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/'
