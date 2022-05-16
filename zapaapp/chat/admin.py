from django.contrib import admin
from chat.models import Canal, Mensaje, Usuario
 
# Register your models here.
admin.site.register(Canal)
admin.site.register(Mensaje)
admin.site.register(Usuario)
