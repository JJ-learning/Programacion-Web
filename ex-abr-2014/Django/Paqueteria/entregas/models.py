from django.db import models

# Create your models here

# Un destinatario es una persona a la que se debe entregar un paquete
class Destinatario(models.Model):
	direccion = models.CharField(max_length=100)
	ciudad = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar
