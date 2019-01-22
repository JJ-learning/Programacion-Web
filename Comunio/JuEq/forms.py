from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from JuEq.models import Jugador, Equipo, Partido
from django.db import models

class loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget= forms.PasswordInput())
	
class SignUpForm(UserCreationForm):
	username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'User'}))
	password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
	class Meta:
		model = User
		fields = [ 'username', 'password1', 'password2']

class JugadorForm(forms.ModelForm):
	nombre_jugador = models.CharField(max_length=50)
	ciudad_natal = models.CharField(max_length=50)
	edad_jugador = models.IntegerField()
	fecha_nacimiento = models.DateField()
	posicion_jugador = models.CharField(max_length=50)
	historia_jugador = models.CharField(max_length=140)
	equipo_jugador = models.ForeignKey(Equipo)
	equipos_anteriores = models.IntegerField()
	class Meta:
		model = Jugador
		fields = ['nombre_jugador', 'ciudad_natal', 'edad_jugador', 'fecha_nacimiento', 'posicion_jugador', 'historia_jugador', 'equipo_jugador', 'equipos_anteriores']

class EquipoForm(forms.ModelForm):
	nombre_equipo = models.CharField(max_length=50)
	ciudad_equipo = models.CharField(max_length=50)
	anio_creacion = models.DateField()
	historia_equipo = models.CharField(max_length=140)
	entrenador_equipo = models.CharField(max_length=50)
	class Meta:
		model = Equipo
		fields = ['nombre_equipo', 'ciudad_equipo', 'anio_creacion', 'historia_equipo', 'entrenador_equipo']


class JornadaForm(forms.ModelForm):
	local = models.ForeignKey(Equipo, related_name="local")
	visitante = models.ForeignKey(Equipo, related_name="visitante")
	goles_local = models.IntegerField()
	goles_visitante = models.IntegerField()
	class Meta:
		model=Partido
		fields = ['local', 'visitante', 'goles_local', 'goles_visitante']