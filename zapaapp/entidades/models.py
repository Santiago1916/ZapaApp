from django.db import models


class Mensaje(models.Model):
    contenido = models.TextField()
    emisor = models.AutoField(primary_key=False)
    receptor = models.AutoField(primary_key=False)
    fecha = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):
    nombre = models.TextField()
    email = models.TextField()
    password = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_login = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

# mod en pgadmin chat_usuario para not null fechas 

class Canal(models.Model):
    nombre = models.TextField()
    mensajes = models.ManyToManyField(Mensaje)
    usuarios = models.ManyToManyField(Usuario)
    descripcion = models.TextField()

    
