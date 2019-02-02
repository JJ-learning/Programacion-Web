from django.db import models

# Create your models here.
class Destino(models.Model):
	ciudad = models.CharField(max_length=30)
	pais = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=140)

	def __str__(self):
		return self.ciudad
		return self.pais
		return self.descripcion

class Viaje(models.Model):
	destino = models.ForeignKey(Destino)
	dias_viaje = models.IntegerField()
	coste_viaje = models.IntegerField()
	modo = models.CharField(max_length=20)


	def __str__(self):
		return self.destino.pais
		return self.dias_viaje
		return self.coste_viaje
		return self.modo
		

class Ruta(models.Model):
	nombre_ruta = models.CharField(max_length=30)
	destino1 = models.ForeignKey(Destino, related_name="destino1")
	destino2 = models.ForeignKey(Destino, related_name="destino2")
	destino3 = models.ForeignKey(Destino, related_name="destino3")
	coste_ruta = models.IntegerField()
	dias_ruta = models.IntegerField()

	def __str__(self):
		return self.nombre_ruta
		return destino1.pais
		return destino2.pais
		return destino3.pais
		return coste_ruta
		return dias_ruta



		