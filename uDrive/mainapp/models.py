from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200) #in db it is varchar
    price = models.FloatField() # in db it is int
    img = models.ImageField(upload_to='cars/')
    fuel = models.CharField(max_length=50,
                            choices=(
                                 ('petrol','petrol'),
                                 ('diesel', 'diesel'),
                                 ('ev','ev')
                            ),
                            default='petrol'
                            )
    transmission = models.CharField(max_length=50, default='Manual')
    seat = models.CharField(max_length=50, default='5 seater')
    year = models.IntegerField(default=2000)
    desc = models.CharField(max_length=200, default='')
    caption = models.CharField(max_length=200, default='')

    def __str__(self):
         return f"car : {self.name}"
