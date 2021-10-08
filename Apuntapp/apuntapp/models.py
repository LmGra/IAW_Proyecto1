from django.db import models


class Autor(models.Model):
    idAutor = models.IntegerField(primary_key=True)
    nomAutor = models.CharField(max_length=50)


class Ficheros(models.Model):
    idFichero = models.IntegerField(primary_key=True)
    nomFichero = models.CharField(max_length=20)
    #capFichero = models.IntegerField(default=0)


class Temario(models.Model):
    idTemario = models.IntegerField(primary_key=True)
    nomTemario = models.CharField(max_length=16)
    nTemario = models.IntegerField(default=0)

class Asignatura(models.Model):
    idAsignatura = models.IntegerField(primary_key=True)
    nomAsignatura = models.CharField(max_length=16)