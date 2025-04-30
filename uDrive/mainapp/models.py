from django.db import models

# Create your models here.
class   Product(models.Model):
    name = models.CharField(max_length=200) #in db it is varchar
    price = models.FloatField() # in db it is int
    img = models.ImageField(upload_to='products/')
