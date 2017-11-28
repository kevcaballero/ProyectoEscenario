#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from .forms import loginForm
from django.shortcuts import redirect
from .models import Escenario
from .models import Evento
from .forms import datosEvento
from .forms import datosComentario
from .forms import datosEscenario
from .models import PresentacionEscenario
from .forms import presEscenario
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .forms import presEscenario


def login_user(request):
    """
    Función para logear usuario, si esta autenticado envia directo al dashboard
    si no valida los campos, verifica que el usuario exista y este activo y envia
    al dashboard de lo contrario envia el mensaje 'Usuario y/o Password incorrectos'
    """
    mensaje = ""
    if request.user.is_authenticated():
        return redirect('reserva:administrar')
    else:
        if request.method == "POST":
            form = loginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('reserva:administrar')
            else:
                mensaje = "Usuario y/o Password incorrectos"

        form = loginForm()
        ctx = {'form': form, 'mensaje': mensaje}
        return render(request, 'reserva/login.html', ctx)


def logout_def(request):
    """
    Función para salir de la aplicación
    """
    logout(request)
    return redirect("reserva:login_user")


@login_required
def administrar(request):
    """
    Función que lleva al dashboard de la aplicación
    """
    lista_escenarios = Escenario.objects.all()
    return render_to_response('reserva/admin.html',
                              {'lista_escenarios': lista_escenarios})


@login_required
def listarEscenario(request):
    return render_to_response('reserva/escenarios.html',
                              {'lista_escenarios': Escenario.objects.all(),
                               'messages': messages.get_messages(request)})


@login_required
def agregarEscenario(request):
    """
    Agrega un escenario nuevo
    """

    if request.method == 'POST':
        form = datosEscenario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El escenario ha sido guardado!")
            return redirect(reverse('reserva:listarEscenario'))
    else:
        form = datosEscenario()
    return render(request, 'reserva/altaEscenario.html', {'form': form})


@login_required
def actualizarEscenario(request, idescenario):
    """
    Actualiza el escenario existente
    """
    instance = get_object_or_404(Escenario, id=idescenario)
    form = datosEscenario(request.POST, request.FILES, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El escenario ha sido actualizado!")
            return redirect(reverse('reserva:listarEscenario'))
    else:
        form = datosEscenario(instance=instance)
    return render(request, 'reserva/altaEscenario.html', {
        'form': form, 'instance': instance
    })


def eliminarEscenario(request, idescenario):
    print(idescenario)
    escenario = get_object_or_404(Escenario, id=idescenario)
    escenario.delete()
    messages.add_message(request, messages.SUCCESS, "El escenario ha sido eliminado con exito")
    return redirect(reverse('reserva:listarEscenario'))


def listarPresentacion(request):
    ctx = {
        "lista_presentaciones": PresentacionEscenario.objects.all(),
        "messages": messages.get_messages(request)
    }
    return render_to_response('reserva/presentaciones.html', ctx)


def agregarPresentacion(request):
    if request.method == 'POST':
        form = presEscenario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La presentacion ha sido guardada!")
            return redirect(reverse('reserva:listarPresentacion'))
    else:
        form = presEscenario()
    return render(request, 'reserva/altaPresentacion.html', {'form': form})


# def actualizarPresentacion(request, idimg):
#     instance = get_object_or_404(PresentacionEscenario, id=idimg)
#     print(instance)
#     form = presEscenario(request.POST, request.FILES, instance=instance)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "La presentacion ha sido actualizada!")
#             return redirect(reverse('reserva:listarPresentacion'))
#     else:
#         form = presEscenario(instance=instance)
#     return render(request, 'reserva/altaPresentacion.html', {
#         'form': form, 'instance': instance
#     })
class actualizarPresentacion(UpdateView):
    model = PresentacionEscenario
    form_class = presEscenario
    template_name = 'reserva/editarPresentacion.html'

    def get_success_url(self):
        return reverse_lazy('reserva:listarPresentacion')


def eliminarPresentacion(request, idimg):
    instance = get_object_or_404(PresentacionEscenario, id=idimg)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "La presentacion ha sido eliminado con exito")
    return redirect(reverse('reserva:listarPresentacion'))


def prinEventos(request):
    lista_escenarios = Escenario.objects.all()
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
            # evento = form.cleaned_data['nombre_evento']
            form.save()  # Guardar los datos en la base de datos
            formPresentaciones.save()
            # return render(request, 'home.html', { 'evento', evento })
    else:
        form = datosEvento()
        formPresentaciones = presEscenario()  #
    return render_to_response('reserva/eventoProgramado.html',
                              {'form': form,
                               'lista_escenarios': lista_escenarios, })


def confirmarEvento(request):
    car_evento = Evento.objects.all()
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
        # Formulario lleno, pero con datos NO validos
        if form.is_valid() and formPresentaciones.is_valid():
            # evento = form.cleaned_data['nombre_evento']
            form.save()
            formPresentaciones.save()  # Guardar los datos en la base de datos
            # return render(request, 'home.html', { 'evento', evento })
    else:
        form = datosEvento()
        formPresentaciones = presEscenario()  #

    return render_to_response('eventoNProgramado.html',
                              {'form': form,
                               'car_evento': car_evento, })


def observacionesEvento(request):
    if request.method == 'POST':
        form = datosComentario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = datosComentario()
        return render_to_response('retroEvento.html', {
            'form': form})


def requerimientos(request):
    car_evento = Evento.objects.all()
    return render_to_response(
        'areas.html',
        {'car_evento': car_evento,
         }

    )


class EventosList(TemplateView):
    template_name = 'reserva/listas_eventos.html'

    def get_context_data(self, **kwargs):
        context = super(EventosList, self).get_context_data(**kwargs)
        context["eventos"] = Evento.objects.all()
        return context


class EventoDetail(DetailView):
    model = Evento
    template_name = 'reserva/detalle_evento.html'
    context_object_name = 'e'


class EventoUpdate(UpdateView):
    model = Evento
    template_name = 'reserva/update_evento.html'
    form_class = datosEvento

    def get_success_url(self):
        return reverse_lazy('reserva:listar_eventos')


class EventoCreate(CreateView):
    pass
