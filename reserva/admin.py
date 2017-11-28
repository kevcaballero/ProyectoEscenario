from django.contrib import admin
from .models import Escenario, PresentacionEscenario, Evento, Comentario

# Register your models here.

admin.site.register(Escenario)
admin.site.register(PresentacionEscenario)
admin.site.register(Evento)
admin.site.register(Comentario)

