from django.contrib import admin

#importing the necessary models of the app here
from .models import Car

# Register your models here.
admin.site.register(Car)
