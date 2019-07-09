from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        """Django uses this when it needs to convert the object to string"""

        return self.user