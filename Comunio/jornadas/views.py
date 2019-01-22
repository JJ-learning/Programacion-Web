from django.shortcuts import render, HttpResponse, loader, get_object_or_404, redirect
from JuEq.models import Equipo, Jugador, Partido
from JuEq.forms import JornadaForm

def jornada(request):
	lista_equipo = Equipo.objects.order_by('anio_creacion')
	if request.method== "POST":
		form = JornadaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/clasificacion')
	else:
		form=JornadaForm()

	context={
		'lista_equipo':lista_equipo,
		'form':form,
	}
	template= loader.get_template('jornadas/jornada.html')
	return HttpResponse(template.render(context, request))

def resultado(request):
	lista_partido = Partido.objects.order_by('id')
	lista_equipo = Equipo.objects.order_by('anio_creacion')
	lista_equipos = Equipo.objects.order_by('nombre_equipo')
	partidos = Partido.objects.all()
	for equipo in lista_equipos:
		for partido in partidos:
			if partido.local.nombre_equipo == equipo.nombre_equipo:
				if partido.goles_local > partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.victorias = equipo.victorias+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_local
					equipo.goles_contra = equipo.goles_contra+partido.goles_visitante
				elif partido.goles_local == partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.empates = equipo.empates+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_local
					equipo.goles_contra = equipo.goles_contra+partido.goles_visitante
				elif partido.goles_local < partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.derrotas = equipo.derrotas+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_local
					equipo.goles_contra = equipo.goles_contra+partido.goles_visitante
			if partido.visitante.nombre_equipo == equipo.nombre_equipo:
				if partido.goles_local < partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.victorias = equipo.victorias+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_visitante
					equipo.goles_contra = equipo.goles_contra+partido.goles_local
				elif partido.goles_local == partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.empates = equipo.empates+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_visitante
					equipo.goles_contra = equipo.goles_contra+partido.goles_local
				elif partido.goles_local > partido.goles_visitante:
					equipo.partidos_jugados = equipo.partidos_jugados+1
					equipo.derrotas = equipo.derrotas+1
					equipo.goles_favor = equipo.goles_favor+partido.goles_visitante
					equipo.goles_contra = equipo.goles_contra+partido.goles_local
		equipo.save()
	context = {
		'lista_equipo':lista_equipo,
		'lista_equipos':lista_equipos,
		'lista_partido':lista_partido,
		'partidos':partidos,
	}
	template = loader.get_template('jornadas/resultado.html')
	return HttpResponse(template.render(context, request))

def borrarResu(request):
	partidos = Partido.objects.all()

	partidos.delete()
	return redirect('/clasificacion')
	context={
		'partidos':partidos,
	}
	template = loader.get_template('jornadas/borrarResu.html')
	return HttpResponse(template.render(context, request))