from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$', views.login_user, name='login_user'),
    url(r'^administrar/$', views.administrar, name='administrar'),
    url(r'^escenarios/lista/$',views.listarEscenario,name='listarEscenario'),
    url(r'^escenarios/agregar/$',views.agregarEscenario,name='agregarEscenario'),
    url(r'^escenarios/(?P<idescenario>\d+)//$',views.actualizarEscenario,name='actualizarEscenario'),
    url(r'^escenarios/(?P<idescenario>\d+)/eliminar/$',views.eliminarEscenario,name='eliminarEscenario'),
    url(r'^presentaciones/lista/$',views.listarPresentacion,name='listarPresentacion'),
    url(r'^presentaciones/agregar/$',views.agregarPresentacion,name='agregarPresentacion'),
    url(r'^presentaciones/(?P<idimg>\d+)/$',views.actualizarPresentacion,name='actualizarPresentacion'),
    url(r'^presentaciones/(?P<idimg>\d+)/eliminar/$',views.eliminarPresentacion,name='eliminarPresentacion'),
    url(r'^agregarPresentacion/$',views.agregarPresentacion,name='agregarPresentacion'),
    url(r'^reservarEvento/$',views.reservarEvento,name='reservarEvento'),
    url(r'^confirmarEvento/$',views.confirmarEvento,name='confirmarEvento'),
    url(r'^requerimientos/$',views.requerimientos,name='requerimientos'),
    url(r'^prinEventos/$', views.prinEventos, name='prinEventos'),
    url(r'^observacionesEvento/$', views.observacionesEvento, name='observacionesEvento'),
]
