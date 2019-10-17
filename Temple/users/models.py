from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser1(AbstractUser):
    age = models.PositiveIntegerField(default=0)