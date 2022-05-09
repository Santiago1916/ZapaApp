from django.db import models

# Create your models here.


class Mensaje(models.Model):
    contenido = models.TextField()
    emisor = models.textField()
    receptor = models.textField()
    fecha = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):
    nombre = models.TextField()
    email = models.TextField()
    password = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_login = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)


class Canal(models.Model):
    nombre = models.TextField()
    mensajes = models.ManyToManyField(Mensaje)
