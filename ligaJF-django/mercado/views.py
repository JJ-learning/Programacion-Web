from django.shortcuts import render, HttpResponse, loader, redirect
from JuEq.models import Equipo, Jugador, Partido, Mercado

import random
# Create your views here.


def mercado(request):
	lista_mercado = Mercado.objects.order_by('valor_apuesta')
	lista_jugadores = Jugador.objects.all()
	jugador = random.choice(lista_jugadores)
	valor = random.randint(120000, 90000000)
	
	mercado = Mercado()
	mercado.jugador = jugador
	mercado.valor_apuesta = valor

	mercado.save()
	context={
		'lista_mercado':lista_mercado,
		'lista_jugadores':lista_jugadores,
		'mercado':mercado,
		'jugador':jugador,
		'valor':valor,
	}
	template=loader.get_template('mercado/mercado.html')
	return HttpResponse(template.render(context, request))

def comprar(request):
	lista_mercado = Mercado.objects.order_by('valor_apuesta')
	lista_equipo = Equipo.objects.order_by('nombre_equipo')

	jugadorM = random.choice(lista_mercado)
	equipo_sale = jugadorM.jugador.equipo_jugador
	equipo_entra = random.choice(lista_equipo)

	jugador2=Jugador()
	jugador2.nombre_jugador = jugadorM.jugador.nombre_jugador
	jugador2.ciudad_natal = jugadorM.jugador.ciudad_natal
	jugador2.edad_jugador = jugadorM.jugador.edad_jugador
	jugador2.fecha_nacimiento = jugadorM.jugador.fecha_nacimiento
	jugador2.posicion = jugadorM.jugador.posicion
	jugador2.equipo_jugador = equipo_entra
	jugador2.puntos_jugador = jugadorM.jugador.puntos_jugador
	jugador2.valor_jugador = jugadorM.valor_apuesta
	jugador2.goles_jugador = jugadorM.jugador.goles_jugador

	jugador2.save()
	jugadorM.jugador.delete()

	context={
		'lista_mercado':lista_mercado,
		'lista_equipo':lista_equipo,
		'jugadorM':jugadorM,
		'equipo_sale':equipo_sale,
		'equipo_entra':equipo_entra,
		'jugador2':jugador2,
	}
	template=loader.get_template('mercado/comprar.html')
	return HttpResponse(template.render(context, request))