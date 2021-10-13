from django.contrib import admin

from .models import Autor, Modulo, Publicacion, Ciclo

admin.site.register(Autor)
admin.site.register(Modulo)
admin.site.register(Publicacion)
admin.site.register(Ciclo)
#admin.site.register(Asignatura)