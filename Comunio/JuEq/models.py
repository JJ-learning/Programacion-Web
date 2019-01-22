from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Equipo(models.Model):
	nombre_equipo = models.CharField(max_length=50)
	ciudad_equipo = models.CharField(max_length=50)
	anio_creacion = models.DateField()
	historia_equipo = models.CharField(max_length=140)
	entrenador_equipo = models.CharField(max_length=50)
	partidos_jugados = models.IntegerField(default=0)
	victorias = models.IntegerField(default=0)
	empates = models.IntegerField(default=0)
	derrotas = models.IntegerField(default=0)
	goles_favor = models.IntegerField(default=0)
	goles_contra = models.IntegerField(default=0)

	def __str__(self):
		return self.nombre_equipo
		return self.ciudad_equipo
		return self.anio_creacion
		return self.historia_equipo
		return self.entrenador_equipo


class Jugador(models.Model):
	nombre_jugador = models.CharField(max_length=50)
	ciudad_natal = models.CharField(max_length=50)
	edad_jugador = models.IntegerField()
	fecha_nacimiento = models.DateField()
	posicion_jugador = models.CharField(max_length=50)
	historia_jugador = models.CharField(max_length=140)
	equipo_jugador = models.ForeignKey(Equipo)
	equipos_anteriores = models.IntegerField()
	puntuacion_jugador = models.IntegerField()
	
	def __str__(self):
		return self.nombre_jugador
		return self.ciudad_natal
		return self.edad_jugador
		return self.fecha_nacimiento
		return self.posicion_jugador
		return self.historia_jugador
		return self.equipo_jugador
		return self.equipos_anteriores

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Partido(models.Model):
	local = models.ForeignKey(Equipo, related_name="local")
	visitante = models.ForeignKey(Equipo, related_name="visitante")
	goles_local = models.IntegerField()
	goles_visitante = models.IntegerField()

	def __str__(self):
		return self.local.nombre_equipo
		return self.visitante.nombre_equipo
		return self.goles_local
		return self.goles_visitante