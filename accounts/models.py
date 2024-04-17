from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return str(f"{self.user}")