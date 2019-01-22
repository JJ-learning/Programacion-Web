from JuEq.models import Equipo, Jugador
from django.shortcuts import render, HttpResponse, loader

def clasificacion(request):
	lista_equipo = Equipo.objects.order_by('anio_creacion')
	lista_equipos = Equipo.objects.order_by('derrotas')
	template=loader.get_template('CaRe/clasificacion.html')
	context={
		'lista_equipos':lista_equipos,
		'lista_equipo': lista_equipo,
	}
	return HttpResponse(template.render(context, request))

# Create your views here.
