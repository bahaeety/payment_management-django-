from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True),
    address = models.CharField(max_length=255, null=True, blank=True),
    date_of_birth = models.DateField(null=True, blank=True)
