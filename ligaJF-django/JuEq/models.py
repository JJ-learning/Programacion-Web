from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Equipo(models.Model):
	nombre_equipo = models.CharField(max_length=50)
	ciudad_equipo = models.CharField(max_length=50)
	entrenador_equipo = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre_equipo
		return self. ciudad_equipo
		return self.entrenador_equipo

class Jugador(models.Model):
	nombre_jugador = models.CharField(max_length=50)
	ciudad_natal = models.CharField(max_length=50)
	edad_jugador = models.IntegerField()
	fecha_nacimiento = models.DateField()
	posicion = models.CharField(max_length=50)
	equipo_jugador = models.ForeignKey(Equipo)
	puntos_jugador = models.IntegerField(default=0)
	valor_jugador = models.IntegerField()
	goles_jugador = models.IntegerField(default=0)

	def __str__(self):
		return self.nombre_jugador
		return self.ciudad_natal
		return self.fecha_nacimiento
		return self.equipo_jugador
		return self.posicion
		return self.puntos_jugador
		return self.valor_jugador

class Partido(models.Model):
	local = models.ForeignKey(Equipo, related_name="local")
	visitante = models.ForeignKey(Equipo, related_name="visitante")
	goles_j_local = models.ForeignKey(Jugador, related_name="goles_j_local")
	goles_j_visitante = models.ForeignKey(Jugador, related_name="goles_j_visitante")
	goles_local = models.IntegerField()
	goles_visitante = models.IntegerField()

	def __str__(self):
		return self.local.nombre_equipo
		return self.visitante.nombre_equipo
		return self.goles_j_local.nombre_jugador
		return self.goles_j_visitante.nombre_jugador
		return self.goles_local
		return self.goles_visitante

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Mercado(models.Model):
	jugador = models.ForeignKey(Jugador)
	valor_apuesta = models.IntegerField()

	def __str__(self):
		return self.jugador.nombre_jugador
		return valor_apuesta

