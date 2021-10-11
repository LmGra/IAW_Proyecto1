from django.contrib import admin

from .models import Autor, Temario, Publicacion, Modulo

admin.site.register(Autor)
admin.site.register(Temario)
admin.site.register(Publicacion)
admin.site.register(Modulo)
#admin.site.register(Asignatura)