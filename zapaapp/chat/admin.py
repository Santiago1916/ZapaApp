from django.contrib import admin
from .models import Canal, Mensaje, Usuario


# Register your models here.
admin.site.register(Canal)
admin.site.register(Mensaje)
admin.site.register(Usuario)



#@admin.register(Usuario)
#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('nombre', 'email', 'password',
#                    'fecha_registro', 'fecha_ultimo_login', 'estado')
