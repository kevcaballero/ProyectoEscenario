from django.contrib import admin
from .models import Escenario

from . import models

# Register your models here.

admin.site.register([
    models.Comentario, models.Escenario, models.Evento, models.ImgEscenario, models.Recurso,
])

