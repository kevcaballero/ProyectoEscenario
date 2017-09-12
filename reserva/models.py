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
    tipo_escenario=models.CharField(max_length=1, choices=TIPO_ESCENARIO, default='Default Value')
    ubicacion= models.CharField(max_length=250)
    estado=models.CharField(max_length=1, choices=ESTADO_ESCENARIO, default=ESTADO_ESCENARIO[1][1])

    def __str__(self):
        return self.nombre_escenario


class ImgEscenario(models.Model):
    presentacion = models.ImageField(upload_to='escenarios',default=' Default Value')#falta algo
    escenario = models.ForeignKey(Escenario)

    def __unicode__(self):
        return self.presentacion

class Evento(models.Model):
    Selecciona=''
    Academico='A'
    Deportivo='D'
    Cultural='CRA'
    Civico='C'
    Recreativo= 'R'
    Capacitacion='CAP'

    TIPO_EVENTO = (

        ('','Selecciona'),
        ('A' ,'Academico'),
        ('D', 'Deportivo'),
        ('CRA','Cultural'),
        ('C' ,'Civico'),
        ('R' ,'Recreativo'),
        ('CAP','Capacitacion')
    )

    nombre_evento =models.CharField(max_length=200)
    capacidad_evento =models.IntegerField(null=True)
    tipo_evento=models.CharField(max_length=3,choices=TIPO_EVENTO)
    objetivo=models.TextField()
    fecha=models.DateField()
    hora= models.DateTimeField()
    medio_difusion=models.FileField()
    req_internet = models.BooleanField()
    img= models.ForeignKey(ImgEscenario)
    escenario= models.ForeignKey(Escenario)
    #organizador=models.ForeignKey(User)#Falta hacer algo



    def __unicode__(self):
        return self.nombre_evento


class Recurso(models.Model):
    DISPONIBILIDAD_EQUIPO = (
        ('P', 'Propio'),
        ('I', 'Institucion'),

    )
    TIPO_EQUIPO = (
        ('L', 'Laptop'),
        ('M', 'MacBook'),

    )
    TIPO_EQUIPOAUDIO = (
        ('M', 'Microfono'),
        ('B', 'Bocina'),

    )
    disponibilidad_equipo =models.CharField(max_length=1,choices=DISPONIBILIDAD_EQUIPO, default='Default Value')
    tipo_equipo=models.CharField(max_length=1, choices=TIPO_EQUIPO,default='Default Value')
    tipo_equipoAudio=models.CharField(max_length=1, choices=TIPO_EQUIPOAUDIO,default='Default Value')


        # Retroalimentacion del Evento
class Comentario(models.Model):
        #user = models.ForeignKey(User) #Falta hacer algo
        evento =models.ForeignKey(Evento)
        contenido= models.TextField()

        def _unicode_(self):
            return " $% $%" %(self.user.username, self.evento.nombre_evento)
