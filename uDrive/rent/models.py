from django.db import models
from mainapp.models import Car
from django.contrib.auth.models import User
# Create your models here.
class RentItem(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def rental_days(self):
        return(self.end_date - self.start_date).days or 1
    def total_price(self):
        return self.rental_days() * self.car.price_per_day
