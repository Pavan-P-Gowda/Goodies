from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    driving_license = models.CharField(max_length=100)
    license_file = models.FileField(upload_to='licenses/', null=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.TextField()

    # Add more fields as needed

    def __str__(self):
        return f"{self.user.username}'s Profile"