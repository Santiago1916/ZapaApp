from multiprocessing.dummy import Array
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Mensaje(models.Model):
    contenido = models.TextField()
    emisor = models.CharField(max_length=256)
    receptor = models.CharField(max_length=256)
    fecha = models.DateTimeField(auto_now_add=True)
    #emisor = models.ForeignKey('auth.Usuario', related_name='mensajes_enviados')
    # auth.?    

class Usuario(models.Model):
    nombre = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_login = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    #mensajes_enviados = models.ManyToManyField(Mensaje, related_name='mensajes_enviados')
    # ni idea aun como implementarlos

    # funcion para obtener info del objeto de una 
    def __str__(self):
        return f'{self.nombre}|{self.email}'+ 'Online' if self.estado else 'Offline' 
# mod en pgadmin chat_usuario para not null fechas


class Canal(models.Model):
    nombre = models.CharField(max_length=256)
    #nuevo
    descripcion = models.CharField(max_length=512)
    mensajes = models.ManyToManyField(Mensaje)
    #nuevo importantisimo campo
    # cambio -/-> usuarios = models.ManyToManyField(Usuario)
    usuarios = ArrayField(
        models.CharField(max_length=256),
        null=True,
    )
    #usuarios = models.ManyToManyField(Usuario)
