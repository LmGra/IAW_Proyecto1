from django.db import models


class Autor(models.Model):
    nomAutor = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=False)
    correo = models.EmailField(default="",blank=False)

    def __str__(self):
        return self.nickname

class Temario(models.Model):

    modulotemario = models.ForeignKey("Modulo", on_delete=models.CASCADE, null=True)

    LISTA_ASIGNATURA = [
        ("IAW+HLC","IAW+HLC"),
        ("SAD","SAD"),
        ("ASGBD","ASGBD"),
        ("SRI","SRI"),
        ("ASO","ASO"),
        ("EIE","EIE"),
        ("PAR","PAR"),
        ("FH","FH"),
        ("GBD","GBD"),
        ("ISO","ISO"),
        ("LMSGI","LMSGI"),
        ("FOL","FOL"),
        ("SI","SI"),
        ("BD","BD"),
        ("PROG","PROG"),
        ("ED","ED"),
        ("AD","AD"),
        ("DI","DI"),
        ("PMDM","PMDM"),
        ("PSP","PSP"),
        ("SGE","SGE"),

    ]

    asignatura = models.CharField('Asignatura', max_length=12, choices=LISTA_ASIGNATURA, blank=False, default="IAW+HLC")
    tema = models.DecimalField('Tema', max_digits=2, decimal_places=0, default=1)


    def __str__(self):
        return self.asignatura+' '+str(self.tema)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50,blank=False,default="")
    texto = models.CharField(max_length=9999,null=True,blank=True)
    archivoFichero = models.FileField(upload_to="archivos/", null=True, blank=True)
    subida = models.ForeignKey("Temario", on_delete=models.CASCADE, null=True)
    autorpublica = models.ForeignKey("Autor", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    LISTA_MODULO = [
        ("ASIR","ASIR"),
        ("DAM","DAM")
    ]

    nombremodulo = models.CharField('NombreModulo', max_length=12, choices=LISTA_MODULO, blank=False, default="ASIR")

    def __str__(self):
        return self.nombremodulo

#class Temario(models.Model):
#    nomTemario = models.CharField(max_length=16)
#class Asignatura(models.Model):
#    nomAsignatura = models.CharField(max_length=16)