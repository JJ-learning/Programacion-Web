from django.conf.urls import url
from . import views


app_name='jornadas'
urlpatterns=[
	url(r'^$', views.jornada, name="jornadas"),
	url(r'^resultado/$', views.resultado, name="resultado"),
	url(r'^borrarResu/$', views.borrarResu, name="borrarResu"),
]