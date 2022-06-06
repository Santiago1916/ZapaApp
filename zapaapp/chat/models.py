from django.db import models
from django.utils import timezone

# Create your models here.
class Canal(models.Model):
    name = models.CharField(max_length=1000)

class Usuario(models.Model):
    username = models.CharField(max_length=1000)
    #canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    password = models.CharField(max_length=1000,blank=True)
    email = models.EmailField(blank=True)


class Mensaje(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000)
    canal = models.CharField(max_length=1000)