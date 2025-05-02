from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200) #in db it is varchar
    price = models.FloatField() # in db it is int
    img = models.ImageField(upload_to='cars/')

    def __str__(self):
         return f"car : {self.name}"
