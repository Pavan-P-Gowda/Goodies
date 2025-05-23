from django.db import models
from mainapp.models import Car
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.
class RentItem(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE, null=True)
    # price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


    @property
    def total_price(self):
        if self.start_date and self.end_date:
            days = (self.end_date - self.start_date).days
            if days <= 0:
                return 0
            return days * self.car.price  # or price_per_day if your Car model has it
        return 0
