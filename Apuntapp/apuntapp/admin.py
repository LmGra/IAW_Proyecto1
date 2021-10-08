from django.contrib import admin

from .models import Autor, Ficheros, Temario, Asignatura

admin.site.register(Autor)
admin.site.register(Ficheros)
admin.site.register(Temario)
admin.site.register(Asignatura)