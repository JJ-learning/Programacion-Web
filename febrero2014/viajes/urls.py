from django.conf.urls import url
from viajes import views
from viajes.views import rutas

app_name='viajes'
urlpatterns = [
	url(r'^$', views.destinos, name="destinos"),
	url(r'^destino/(?P<destino_id>\d+)/$', views.destino, name="destino"),
	url(r'^newD/$', views.newD, name="newD"),
	url(r'^viajes/$',views.viajes, name="viajes"),
	url(r'^newV', views.newV, name="newV"),
	url(r'^viajes/(?P<viaje_id>\d+)/$', views.viaje, name="viaje"),
	url(r'^editar/viajes/(?P<viaje_id>\d+)', views.editarV, name="editarV"),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^logout/', views.logout_view, name="logout"),
	url(r'^rutas/$', rutas.as_view(), name="rutas"),
]