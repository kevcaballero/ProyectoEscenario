from django import  forms
from django.forms import  ModelForm
from .models import Evento
from .models import  Comentario
from .models import ImgEscenario
from .models import Escenario
from django.utils.translation import ugettext_lazy as _


class loginForm(forms.Form):
    username=forms.CharField(max_length=50,
                             widget= forms.TextInput(attrs={
                                 'type':'email'
                             }))
    password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
                                 'type':'password'

                            }))
class datosEscenario(forms.ModelForm):
    class Meta:
        model = Escenario
        fields = ['nombre_escenario','tipo_escenario','ubicacion','estado']
        labels = {
            'nombre_escenario':_('Nombre del escenario'),
            'tipo_escenario':_('Tipo de escenario'),
            'ubicacion':_('Ubicacion del escenario'),
            'estado':_('Estado del escenario'),

        }
        widgets = {
            'nombre_escenario': forms.TextInput(attrs ={'id':'nombre_escenario','class': 'form-group row form-control '}),
            'tipo_escenario': forms.Select(attrs={'id':'tipo_escenario','class': 'form-group row form-control '}),
            'ubicacion': forms.TextInput(attrs={'id':'ubicacion','class': 'form-group row form-control '}),
            'imagen': forms.FileInput(attrs={'id':'imagen','class': 'form-group row form-control '}),
            'estado': forms.Select(attrs={'class': 'form-group row form-control '}),
        }

class datosEvento(forms.ModelForm):
    class Meta:
        model= Evento
        fields=['nombre_evento','capacidad_evento','tipo_evento', 'objetivo','fecha','hora','medio_difusion', 'req_internet','escenario']
        labels = {

            'nombre_evento': _('Nombre del evento:'),
            'escenario':_('Escenario elegido:'),
            'capacidad_evento': _('Capacidad del evento:'),
            'tipo_evento':_('Tipo de Evento:'),
            'objetivo': _('Objetivo del Evento:'),
            'fecha': _('Fecha programada para el evento:'),
            'hora': _('Hora del evento:'),
            'medio_difusion': _('¿Como desea difundir su evento?'),
            'req_internet': _('¿Requiere Internet?'),


        }
        widgets = {

            'nombre_evento': forms.TextInput(attrs={'id':'nombre_evento','class': 'form-group row form-control '}),
            'escenario': forms.Select(attrs={'id':'escenario','class': 'form-group row form-control '}),
            'capacidad_evento': forms.TextInput(attrs={'id':'capacidad_evento','class': 'form-group row form-control'}),
            'tipo_evento': forms.Select(attrs={'id':'tipo_evento' ,'class': 'form-group row form-control','selected':'selected'}),
            'objetivo': forms.Textarea(attrs={'id':'objetivo','class': 'form-group row form-control'}),
            'fecha':forms.DateInput(attrs={'id':'fecha','class': 'form-group row form-control '  }),
            'hora': forms.DateTimeInput(attrs={'id':'hora','class': 'form-group row form-control'}),
            'medio_difusion': forms.FileInput(attrs={'id':'medio_difusion','class': 'form-control-file'}),
            'req_internet': forms.CheckboxInput(attrs={'id':'req_internet','class': ' form-check form-check-input ','type':"checkbox" }),
            'escenario': forms.Select(attrs={'class': 'form-group row form-control '}),

        }

            #VALIDACIONES

        #Validacion de campo nombre_evento

        def clean_nombre_evento(self):
            diccionario_limpio = self.cleaned_data
            nombre_evento = diccionario_limpio.get('nombre_evento')
            if len(nombre_evento) > 200:
                raise forms.ValidationError("El nombre del evento debe ser menor a 200 caracteres")

            return nombre_evento

        def clean_nombre_evento(self):
            diccionario_limpio = self.cleaned_data
            nombre_evento = diccionario_limpio.get('nombre_evento')
            if len(nombre_evento) < 1:
                raise forms.ValidationError("El nombre del evento es obligatorio")

            return nombre_evento
        #Validacion de campo capacidad_evento

        def clean_capacidad_evento(self):
            diccionario_limpio = self.cleaned_data
            capacidad_evento = diccionario_limpio.get('capacidad_evento')
            if len(capacidad_evento) < 1:
                raise  forms.ValidationError("El campo capacidad del evento es obligatorio")

            return capacidad_evento

        def clean_capacidad_evento(self):
            diccionario_limpio = self.cleaned_data
            capacidad_evento = diccionario_limpio.get('capacidad_evento')
            if not capacidad_evento.isalnum():
                raise  forms.ValidationError("El campo solo admite numeros")

            return capacidad_evento


class presEscenario(forms.ModelForm):
    class Meta:
        model=ImgEscenario
        fields =['presentacion','escenario']
        labels ={

            'presentacion': _('¿Como desea acomodar el escenario?'),
            'escenario':_('Nombre de Escenario')

        }
        widgets = {
            'presentacion' : forms.FileInput(attrs={'class': 'form-group row '}),
            'escenario': forms.Select(attrs={'class': 'form-group row form-control ' }),

        }




class datosComentario(forms.ModelForm):
    class Meta:
        model= Comentario
        fields =['contenido']
        labels={


            'contenido': _('Observaciones del evento:')
                }


