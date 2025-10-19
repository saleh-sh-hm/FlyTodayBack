from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    national_ID = models.CharField()
    gender = models.CharField()
    nationality = models.CharField()
    birth_date = models.DateField(null=True, blank=True)
    telephone = models.CharField()
    address = models.CharField()