from django.db import models
from django import forms
from viajes.models import Destino, Viaje
from django.contrib.auth.models import User

class DestinoForm(forms.ModelForm):
	ciudad = models.CharField(max_length=30)
	pais = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=140)
	class Meta:
		model = Destino
		fields = ['ciudad', 'pais', 'descripcion']	

class ViajeForm(forms.ModelForm):
	destino = models.ForeignKey(Destino)
	dias_viaje = models.IntegerField()
	coste_viaje = models.IntegerField()
	modo = models.CharField(max_length=20)
	class Meta:
		model = Viaje
		fields = ['destino', 'dias_viaje', 'coste_viaje', 'modo']


class loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget= forms.PasswordInput())	