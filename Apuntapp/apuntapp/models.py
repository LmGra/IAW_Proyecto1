from django.db import models


class Autor(models.Model):
    idAutor = models.IntegerField()
    nomAutor = models.CharField(max_length=50)


class Ficheros(models.Model):
    idFichero = models.ForeignKey(Fichero, on_delete=models.CASCADE)
    nomFichero = models.CharField(max_length=20)
    #capFichero = models.IntegerField(default=0)


class Temario(models.Model):
    idTemario = models.ForeignKey(Temario, on_delete=models.CASCADE)
    nomTemario = models.CharField(max_length=16)
    nTemario = models.IntegerField(default=0)

class Asignatura(models.Model):
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nomAsignatura = models.CharField(max_length=16)