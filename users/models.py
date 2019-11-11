from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30, blank=True, null=True)
    emergency_contact = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=6)
    birthdate = models.DateField(blank=True, null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.email

    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)