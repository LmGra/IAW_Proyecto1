from django.contrib import admin

from .models import Autor, Asignatura, Publicacion, Ciclo

admin.site.register(Autor)
admin.site.register(Asignatura)
admin.site.register(Publicacion)
admin.site.register(Ciclo)
#admin.site.register(Asignatura)