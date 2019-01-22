from django.conf.urls import url
from . import views


app_name='Clasificacion'
urlpatterns=[
	url(r'^$', views.clasificacion, name="clasificacion"),
	url(r'^partido/$', views.partido, name="partido"),
	url(r'^resultado/$', views.resultado, name="resultado"),
	url(r'^borrarPartido/$', views.borrarPartido, name="borrarPartido"),
]