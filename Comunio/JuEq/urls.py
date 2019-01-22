from django.conf.urls import url
from . import views
from JuEq.views import login

app_name='JuEq'
urlpatterns=[
	url(r'^equipo/(?P<equipo_id>\d+)/$', views.equipos, name="equipos"),
	url(r'^jugador/(?P<jugador_id>\d+)/$', views.jugador, name="jugador"),
	url(r'^jugadores/$', views.jugadores, name="jugadores"),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^$', views.home, name="home"),
	url(r'^newUser/$', views.nuevoUsuario, name="register"),
	url(r'^logout/', views.logout_view, name="logout"),
	url(r'^new/jugador/$', views.nuevoJugador, name="nuevo"),
	url(r'^new/equipo/$', views.nuevoEquipo, name="nequipo"),
	url(r'^editar/jugador/(?P<jugador_id>\d+)/$', views.editarJugador, name="editarJ"),
	url(r'^editar/equipo/(?P<equipo_id>\d+)/$', views.editarEquipo, name="editarE"),
	url(r'^borrar/jugador/(?P<jugador_id>\d+)/$', views.borrarJugador, name="borrarJ"),
	url(r'^borrar/equipo/(?P<equipo_id>\d+)/$', views.borrarEquipo, name="borrarE"),
	url(r'^instrucciones', views.instrucciones, name="instrucciones"),
]