from django import forms
from django.forms import ModelForm
from .models import Evento
from .models import Comentario
from .models import PresentacionEscenario
from .models import Escenario
from django.utils.translation import ugettext_lazy as _


class loginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'type': 'email'
                               }))
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password'

    }))


class datosEscenario(forms.ModelForm):
    class Meta:
        model = Escenario
        fields = ['nombre_escenario', 'tipo_escenario', 'ubicacion', 'estado', 'imagen']
        labels = {
            'nombre_escenario': _('Nombre del escenario'),
            'tipo_escenario': _('Tipo de escenario'),
            'ubicacion': _('Ubicacion del escenario'),
            'estado': _('Estado del escenario'),

        }
        widgets = {
            'nombre_escenario': forms.TextInput(
                attrs={'id': 'nombre_escenario', 'class': 'form-group row form-control '}),
            'tipo_escenario': forms.Select(attrs={'id': 'tipo_escenario', 'class': 'form-group row form-control '}),
            'ubicacion': forms.TextInput(attrs={'id': 'ubicacion', 'class': 'form-group row form-control '}),
            'imagen': forms.FileInput(attrs={'id': 'imagen', 'class': 'form-group row form-control '}),
            'estado': forms.Select(attrs={'class': 'form-group row form-control '}),
        }


class datosEvento(forms.ModelForm):

    class Meta:
        model = Evento
        fields = [
            'nombre_evento',
            'fecha_hora',
            'escenario',
            'presentacion',
            'capacidad_evento',
            'tipo_evento',
            'objetivo',
            'publicar_medios',
            'publicar_sito_web',
            'publicar_social_media',
            'facebook_live',
            'musica_ambiente',
            'laptop',
            'microfonos',
            'internet',
        ]

        widgets = {
            'nombre_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_hora': forms.TextInput(attrs={'class': 'form-control '}),
            'escenario': forms.Select(attrs={'class': 'form-control'}),
            'presentacion': forms.Select(attrs={'class': 'form-control'}),
            'capacidad_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_evento': forms.Select(attrs={'class': 'form-control'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control'}),
            'publicar_medios': forms.Select(attrs={'class': 'form-control'}),
            'publicar_sito_web': forms.Select(attrs={'class': 'form-control'}),
            'publicar_social_media': forms.Select(attrs={'class': 'form-control'}),
            'facebook_live': forms.Select(attrs={'class': 'form-control'}),
            'musica_ambiente': forms.Select(attrs={'class': 'form-control'}),
            'laptop': forms.Select(attrs={'class': 'form-control'}),
            'microfonos': forms.Select(attrs={'class': 'form-control'}),
            'internet': forms.Select(attrs={'class': 'form-control'}),
        }




class presEscenario(forms.ModelForm):

    class Meta:
        model = PresentacionEscenario
        fields = ['nombre', 'presentacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'presentacion': forms.FileInput(attrs={'class': 'form-group row'}),
        }


class datosComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        labels = {

            'contenido': _('Observaciones del evento:')
        }
