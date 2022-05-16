from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.


class Mensaje(models.Model):
    contenido = models.TextField()
    # models.CharField(max_length=256)
    emisor = models.ForeignKey(to=User, on_delete=models.PROTECT, default='no one', related_name='emisor_msg')
    receptor = models.ForeignKey(to=User,on_delete=models.SET_DEFAULT,default='anonymous',)#models.CharField(max_length=256)
    fecha = models.DateTimeField(auto_now_add=True)
    canal_id = models.ForeignKey(to="Canal", on_delete=models.CASCADE, related_name='mensajes',null=True)
    #emisor = models.ForeignKey('auth.Usuario', related_name='mensajes_enviados')
    # auth.?    

class Usuario(models.Model):
    nombre = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_login = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    #mensajes_enviados = models.ManyToManyField(Mensaje, related_name='mensajes_enviados')
    # ni idea aun como implementarlos

    # funcion para obtener info del objeto de una 
    def __str__(self):
        return str(self.nombre)+' # '+str(self.email)+ f"{' - Online' if self.estado else ' - Offline'}"


# mod en pgadmin chat_usuario para not null fechas


class Canal(models.Model):
    nombre = models.CharField(max_length=256)
    #nuevo
    descripcion = models.CharField(max_length=512)
    mensajes = models.ManyToOneRel(to=Mensaje,field='contenido',field_name='mensajes_log')
    #nuevo importantisimo campo
    # cambio -/-> usuarios = models.ManyToManyField(Usuario)
    #usuarios = ArrayField(
    #    models.CharField(max_length=256),
    #    null=True,
    #)
    usuarios = models.ManyToOneRel(
        to=User, field='id', field_name='users')
