from JuEq.models import Equipo, Jugador, Partido
from django.shortcuts import render, HttpResponse, loader, redirect

import random
# Create your views here.

def clasificacion(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	lista_jugadores = Jugador.objects.order_by('-puntos_jugador')
	template=loader.get_template('Clasificacion/clasificacion.html')
	context={
		'lista_jugadores':lista_jugadores,
		'lista_equipo': lista_equipo,
	}
	return HttpResponse(template.render(context, request))

def partido(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	equipo1 = random.choice(lista_equipo)
	equipo2 = random.choice(lista_equipo)
	if equipo1.nombre_equipo == equipo2.nombre_equipo:
		equipo2 = random.choice(lista_equipo)
	jugador1 = Jugador.objects.filter(equipo_jugador=equipo1)
	jugador2 = Jugador.objects.filter(equipo_jugador=equipo2)
	goles1 = random.randrange(6)
	goles2 = random.randrange(6)
	jugador_local = random.choice(jugador1)
	jugador_visitante = random.choice(jugador2)

	partido = Partido()
	partido.local = equipo1
	partido.visitante = equipo2
	partido.goles_local = goles1
	partido.goles_visitante = goles2
	partido.goles_j_local = jugador_local
	partido.goles_j_visitante = jugador_visitante

	partido.save()
	context={
		'lista_equipo':lista_equipo,
		'equipo1':equipo1,
		'equipo2':equipo2,
		'jugador1':jugador1,
		'jugador2':jugador2,
		'goles1':goles1,
		'goles2':goles2,
		'partido':partido,
		'jugador_local':jugador_local,
		'jugador_visitante':jugador_visitante,
		
	}
	template= loader.get_template('Clasificacion/partido.html')
	return HttpResponse(template.render(context, request))

def resultado(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	lista_jugadores = Jugador.objects.order_by('puntos_jugador')
	partidos = Partido.objects.all()

	for jugador in lista_jugadores:
		for partido in partidos:
			if partido.goles_j_local.nombre_jugador == jugador.nombre_jugador:
				jugador.puntos_jugador = jugador.puntos_jugador + (10*partido.goles_local)
				jugador.goles_jugador = jugador.goles_jugador + partido.goles_local
				if partido.goles_local >= 1:
					jugador.valor_jugador = jugador.valor_jugador + (100*partido.goles_local)
				else:
					jugador.valor_jugador = jugador.valor_jugador - 100
			if partido.goles_j_visitante.nombre_jugador == jugador.nombre_jugador:
				jugador.puntos_jugador = jugador.puntos_jugador + (10*partido.goles_visitante)
				jugador.goles_jugador = jugador.goles_jugador + partido.goles_visitante
				if partido.goles_visitante >= 1:
					jugador.valor_jugador = jugador.valor_jugador + (100*partido.goles_visitante)
				else:
					jugador.valor_jugador = jugador.valor_jugador - 100
		jugador.save()
	context={
		'lista_equipo':lista_equipo,
		'lista_jugadores':lista_jugadores,
		'partidos':partidos,
	}
	template = loader.get_template('Clasificacion/resultado.html')
	return HttpResponse(template.render(context, request))

def borrarPartido(request):
	partidos = Partido.objects.all()

	partidos.delete()
	return redirect('/clasificacion')
	context={
		'partidos':partidos,
	}
	template = loader.get_template('Clasificacion/borrarPartido.html')
	return HttpResponse(template.render(context, request))