from django.shortcuts import render_to_response,get_object_or_404, render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from .forms import loginForm
from django.shortcuts import redirect
from .models import Escenario
from .models import Evento
from .forms import datosEvento
from .forms import datosComentario
from .forms import datosEscenario
from .models import  ImgEscenario
from .forms import presEscenario
from django.contrib import  messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import presEscenario
# Create your views here.

def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('reserva:administrar')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reserva:administrar')
        else:
            return redirect('reserva:login_user')


def listarEscenario(request):
    return render_to_response("escenarios.html", {"lista_escenarios": Escenario.objects.all(), "messages": messages.get_messages(request)})




def agregarEscenario(request):

    if request.method == 'POST':
        form = datosEscenario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El escenario ha sido guardado!")
            return redirect(reverse('reserva:listarEscenario'))

    else:
        form=datosEscenario()
    return render(request, 'altaEscenario.html', {'form': form})

def actualizarEscenario(request, idescenario):
    instance= get_object_or_404(Escenario, id=idescenario)
    form=datosEscenario(request.POST ,request.FILES, instance=instance)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El escenario ha sido actualizado!")
            return redirect(reverse('reserva:listarEscenario'))
    else:
        form=datosEscenario(instance=instance)
    return render(request, 'altaEscenario.html',{
                                    'form':form,'instance':instance
                                    })
def eliminarEscenario(request,idescenario):
    instance=get_object_or_404(Escenario, id=idescenario)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El escenario ha sido eliminado con exito" )
    return redirect(reverse('reserva:listarEscenario'))

def listarPresentacion(request):
    return render_to_response("presentaciones.html", {"lista_presentaciones": ImgEscenario.objects.all(), "messages": messages.get_messages(request)})

def agregarPresentacion(request):

    if request.method == 'POST':
        form = presEscenario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La presentacion ha sido guardada!")
            return redirect(reverse('reserva:listarPresentacion'))

    else:
        form=presEscenario()
    return render(request, 'altaPresentacion.html', {'form': form})

def actualizarPresentacion(request, idimg):
    instance= get_object_or_404(ImgEscenario, id=idimg)
    form=presEscenario(request.POST ,request.FILES, instance=instance)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La presentacion ha sido actualizada!")
            return redirect(reverse('reserva:listarPresentacion'))
    else:
        form=datosEscenario(instance=instance)
    return render(request, 'altaPresentacion.html',{
                                    'form':form,'instance':instance
                                    })
def eliminarPresentacion(request,idimg):
    instance=get_object_or_404(ImgEscenario, id=idimg)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "La presentacion ha sido eliminado con exito" )
    return redirect(reverse('reserva:listarPresentacion'))



def prinEventos(request):

    lista_escenarios=Escenario.objects.all()
    return render_to_response(
        'index.html',
        {'lista_escenarios': lista_escenarios,

         })


def reservarEvento(request):
    lista_escenarios = Escenario.objects.all()
    if request.method == 'POST':  # Si el usuario esta enviando el formulario con datos
        nombre_evento = request.POST['nombre_evento']
        capacidad_evento = request.POST['capacidad_evento']
        tipo_evento = request.POST['tipo_evento']
        objetivo = request.POST['objetivo']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        medio_difusion = request.POST['medio_difusion']
        req_internet = request.POST['req_internet']

        presentacion = request.POS['presentacion']
        escenario = request.POST['escenario']

        form = datosEvento(
            {'nombre_evento': nombre_evento, 'capacidad_evento': capacidad_evento, 'tipo_evento': tipo_evento,
             'objetivo': objetivo, 'fecha': fecha, 'hora': hora, 'medio_difusion': medio_difusion,
             'req_internet': req_internet})
        formPresentaciones = presEscenario({'presentacion': presentacion, 'escenario': escenario})


        if form.is_valid():
            #evento = form.cleaned_data['nombre_evento']
            form.save()  # Guardar los datos en la base de datos
            formPresentaciones.save()
            #return render(request, 'home.html', { 'evento', evento })
    else:
        form = datosEvento()
        formPresentaciones = presEscenario()#
    return render_to_response('eventoProgramado.html',
                                  {'form': form,
                                   'lista_escenarios': lista_escenarios,})



def confirmarEvento(request):
    car_evento = Evento.objects.all()
    if request.method == 'POST':  # Si el usuario esta enviando el formulario con datos
        nombre_evento= request.POST['nombre_evento']
        capacidad_evento =request.POST['capacidad_evento']
        tipo_evento=request.POST['tipo_evento']
        objetivo=request.POST['objetivo']
        fecha=request.POST['fecha']
        hora=request.POST['hora']
        medio_difusion=request.POST['medio_difusion']
        req_internet=request.POST['req_internet']

        presentacion=request.POS['presentacion']
        escenario=request.POST['escenario']

        form = datosEvento({'nombre_evento':nombre_evento,'capacidad_evento':capacidad_evento,'tipo_evento':tipo_evento,
                            'objetivo':objetivo,'fecha':fecha,'hora':hora,'medio_difusion':medio_difusion,'req_internet':req_internet})
        formPresentaciones = presEscenario({'presentacion':presentacion,'escenario':escenario})
         # Formulario lleno, pero con datos NO validos
        if form.is_valid() and formPresentaciones.is_valid() :
            #evento = form.cleaned_data['nombre_evento']
            form.save()
            formPresentaciones.save()# Guardar los datos en la base de datos
            #return render(request, 'home.html', { 'evento', evento })
    else:
        form = datosEvento()
        formPresentaciones = presEscenario()#



    return render_to_response('eventoNProgramado.html',
                                  {'form': form,
                                   'car_evento': car_evento,})



def observacionesEvento(request):
    if request.method == 'POST':
        form =datosComentario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=datosComentario()
        return render_to_response('retroEvento.html',{
                                    'form':form})




def administrar(request):
    lista_escenarios=Escenario.objects.all()
    return render_to_response(
        'admin.html',
        {'lista_escenarios': lista_escenarios,

         })
def requerimientos(request):

    car_evento=Evento.objects.all()
    return render_to_response(
        'areas.html',
        {'car_evento':car_evento,
        }

    )
