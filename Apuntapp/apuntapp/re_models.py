from django.db import models


class Autor(models.Model):

    nickname = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.nickname

class Modulo(models.Model):

    ciclo = models.ForeignKey("Ciclo", on_delete=models.CASCADE, null=True)

    LISTA_Modulo_ASIR = [

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
        ("FOL","Formación y Orientación Laboral")
    ]

    LISTA_Modulo_DAM = [

        ("SI","Sistemas Informáticos"),
        ("BD","Base de Datos"),
        ("PROG","Programación"),
        ("ED","Entorno de Desarrollo"),
        ("AD","Acceso a Datos"),
        ("DI","Desarrollo de Interfaces"),
        ("PMDM","Programación Multimedia y Dispositivos Móviles"),
        ("PSP","Programación de Servicios y Procesos"),
        ("SGE","Sistemas de Gestión Empresarial"),
        ("FOL","Formación y Orientación Laboral"),
        ("EIE","Empresa e Iniciativa Emprendedora")
    ]

    LISTA_Modulo_SMR = [

        ("MME","Montaje y Mantenimiento de Equipos"),
        ("SOM","Sistemas Operativos Monopuesto"),
        ("AO","Aplicaciones Ofimáticas"),
        ("RL","Redes Locales"),
        ("SOR","Sistemas Operativos en Red"),
        ("SI","Seguridad Informática"),
        ("SR","Servicios en Red"),
        ("AW","Aplicaciones Web"),
        ("FOL","Formación y Orientación Laboral"),
        ("EIE","Empresa e Iniciativa Emprendedora")

    ]

    modulo_asir = models.CharField('Modulo Asir', max_length=64, choices=LISTA_Modulo_ASIR, blank=False, default="IAW+HLC")
    modulo_dam = models.CharField('Modulo Dam', max_length=64, choices=LISTA_Modulo_DAM, blank=False, default="BD")
    modulo_smr = models.CharField('Modulo Smr', max_length=64, choices=LISTA_Modulo_SMR, blank=False, default="FOL")

    tema = models.DecimalField('Tema', max_digits=2, decimal_places=0, default=1)


    def __str__(self):
        return self.modulo+' '+str(self.tema)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50,blank=False,default="")
    comentario = models.CharField(max_length=300,null=True,blank=True)
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    modulo_asir = models.ForeignKey("Modulo Asir", on_delete=models.CASCADE, null=True)
    modulo_dam = models.ForeignKey("Modulo Dam", on_delete=models.CASCADE, null=True)
    modulo_smr = models.ForeignKey("Modulo Smr", on_delete=models.CASCADE, null=True)
    autor = models.ForeignKey("Autor", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class Ciclo(models.Model):
    LISTA_Ciclo = [
        ("ASIR","Administración de Sistemas Informáticos en Red"),
        ("DAM","Desarrollo de Aplicaciones Multiplataforma"),
        ("SMR","Sistemas Microinformáticos y Redes")
    ]

    ciclo = models.CharField('Ciclo', max_length=12, choices=LISTA_Ciclo, blank=False, default="ASIR")

    def __str__(self):
        return self.ciclo

#class Modulo(models.Model):
#    nomModulo = models.CharField(max_length=16)
#class Modulo(models.Model):
#    nomModulo = models.CharField(max_length=16)