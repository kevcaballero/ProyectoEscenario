from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Escenario(models.Model):
    TIPO_ESCENARIO = (
        ('O', 'Operativo'),
        ('A', 'Academico'),
        ('D', 'Deportivo'),
        ('C', 'Civico'),
        ('P', 'Pasillos'),
        ('R', 'Recreativo'),
    )

    ESTADO_ESCENARIO = (
        ('O', 'Ocupado'),
        ('D', 'Disponible'),
    )

    nombre_escenario = models.CharField(max_length=200)
    tipo_escenario = models.CharField(max_length=1, choices=TIPO_ESCENARIO, default='Default Value')
    ubicacion = models.CharField(max_length=250)
    estado = models.CharField(max_length=1, choices=ESTADO_ESCENARIO, default=ESTADO_ESCENARIO[1][1])
    imagen = models.ImageField(upload_to='escenarios', blank=True, null=True)

    def __str__(self):
        return self.nombre_escenario


class PresentacionEscenario(models.Model):
    nombre = models.CharField("Nombre de la presentacion", max_length=100)
    presentacion = models.ImageField(upload_to='presentacion')
    # escenario = models.CharField("Tmp", max_length=100)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    Academico = 'A'
    Deportivo = 'D'
    Cultural = 'CRA'
    Civico = 'C'
    Recreativo = 'R'
    Capacitacion = 'CAP'

    TIPO_EVENTO = (
        ('A', 'Academico'),
        ('D', 'Deportivo'),
        ('CRA', 'Cultural'),
        ('C', 'Civico'),
        ('R', 'Recreativo'),
        ('CAP', 'Capacitacion')
    )

    OPTIONS_CHOICES = (
        ('SI', 'SI'),
        ('NO', 'NO')
    )

    nombre_evento = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField("Fecha y hora del evento")
    escenario = models.ForeignKey(Escenario)
    presentacion = models.ForeignKey(PresentacionEscenario)
    capacidad_evento = models.IntegerField("Capacidad del evento", null=True)
    tipo_evento = models.CharField(max_length=3, choices=TIPO_EVENTO)
    objetivo = models.TextField("Objetivo")
    publicar_medios = models.CharField("Publicar en medios?", max_length=2, choices=OPTIONS_CHOICES)
    publicar_sito_web = models.CharField("Publicar en sitio web?", max_length=2, choices=OPTIONS_CHOICES)
    publicar_social_media = models.CharField("Publicar en redes sociales?", max_length=2, choices=OPTIONS_CHOICES)
    facebook_live = models.CharField("Transmitir en tiempo real (Facebook live)?", max_length=2,
                                     choices=OPTIONS_CHOICES)
    musica_ambiente = models.CharField("Música de ambiente?", max_length=2, choices=OPTIONS_CHOICES)
    laptop = models.CharField("Requiere laptop?", max_length=2, choices=OPTIONS_CHOICES)
    microfonos = models.CharField("Requiere microfonos?", max_length=2, choices=OPTIONS_CHOICES)
    internet = models.CharField(max_length=2, choices=OPTIONS_CHOICES)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.nombre_evento


# class Recurso(models.Model):
#     DISPONIBILIDAD_EQUIPO = (
#         ('P', 'Propio'),
#         ('I', 'Institucion'),
#
#     )
#     TIPO_EQUIPO = (
#         ('L', 'Laptop'),
#         ('M', 'MacBook'),
#
#     )
#     TIPO_EQUIPOAUDIO = (
#         ('M', 'Microfono'),
#         ('B', 'Bocina'),
#
#     )
#     disponibilidad_equipo = models.CharField(max_length=1, choices=DISPONIBILIDAD_EQUIPO, default='Default Value')
#     tipo_equipo = models.CharField(max_length=1, choices=TIPO_EQUIPO, default='Default Value')
#     tipo_equipoAudio = models.CharField(max_length=1, choices=TIPO_EQUIPOAUDIO, default='Default Value')


class Comentario(models.Model):
    # user = models.ForeignKey(User) #Falta hacer algo
    evento = models.ForeignKey(Evento)
    contenido = models.TextField()

    def _unicode_(self):
        return " $% $%" % (self.user.username, self.evento.nombre_evento)
