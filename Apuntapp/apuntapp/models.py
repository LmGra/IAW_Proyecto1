from django.db import models


class Autor(models.Model):
    nomAutor = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=False)
    correo = models.EmailField(default="",blank=False)

    def __str__(self):
        return self.nickname

class Asignatura(models.Model):

    CicloAsignatura = models.ForeignKey("Ciclo", on_delete=models.CASCADE, null=True)

    LISTA_ASIGNATURA = [
        ("IAW+HLC","Implantación de Aplicaciones Web + Hora libre configuración"),
        ("SAD","Seguridad y Alta Disponibilidad"),
        ("ASGBD","Administración de Sistemas Gestores de Bases de Datos"),
        ("SRI","Servicios de Red e Internet"),
        ("ASO","Administración de Sistemas Operativos"),
        ("EIE","Empresa e Iniciativa Emprendedora"),
        ("PAR","Planificación y Administración de Redes"),
        ("FH","Fundamentos Hardware"),
        ("GBD","Gestión de Bases de Datos"),
        ("ISO","Implantación de Sistemas Operativos"),
        ("LMSGI","Lenguaje de Marcas y Sistemas de Gestión de información"),
        ("FOL","Formación y Orientación Laboral"),
        ("SI","Sistemas Informáticos"),
        ("BD","Base de Datos"),
        ("PROG","Programación"),
        ("ED","Entorno de Desarrollo"),
        ("AD","Acceso a Datos"),
        ("DI","Desarrollo de Interfaces"),
        ("PMDM","Programación Multimedia y Dispositivos Móviles"),
        ("PSP","Programación de Servicios y Procesos"),
        ("SGE","Sistemas de Gestión Empresarial"),
        ("MME","Montaje y Mantenimiento de Equipos"),
        ("SOM","Sistemas Operativos Monopuesto"),
        ("AO","Aplicaciones Ofimáticas"),
        ("RL","Redes Locales"),
        ("SOR","Sistemas Operativos en Red"),
        ("SI","Seguridad Informática"),
        ("SR","Servicios en Red"),
        ("AW","Aplicaciones Web")

    ]

    asignatura = models.CharField('Asignatura', max_length=64, choices=LISTA_ASIGNATURA, blank=False, default="IAW+HLC")
    tema = models.DecimalField('Tema', max_digits=2, decimal_places=0, default=1)


    def __str__(self):
        return self.asignatura+' '+str(self.tema)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50,blank=False,default="")
    texto = models.CharField(max_length=9999,null=True,blank=True)
    archivoFichero = models.FileField(upload_to="archivos/", null=True, blank=True)
    subida = models.ForeignKey("Asignatura", on_delete=models.CASCADE, null=True)
    autorpublica = models.ForeignKey("Autor", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class Ciclo(models.Model):
    LISTA_Ciclo = [
        ("ASIR","Administración de Sistemas Informáticos en Red"),
        ("DAM","Desarrollo de Aplicaciones Multiplataforma"),
        ("SMR","Sistemas Microinformáticos y Redes")
    ]

    nombreCiclo = models.CharField('NombreCiclo', max_length=12, choices=LISTA_Ciclo, blank=False, default="ASIR")

    def __str__(self):
        return self.nombreCiclo

#class Asignatura(models.Model):
#    nomAsignatura = models.CharField(max_length=16)
#class Asignatura(models.Model):
#    nomAsignatura = models.CharField(max_length=16)