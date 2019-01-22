from django.db import models
from django import forms
from JuEq.models import Jugador, Equipo, Partido
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class JugadorForm(forms.ModelForm):
	nombre_jugador = models.CharField(max_length=50)
	ciudad_natal = models.CharField(max_length=50)
	edad_jugador = models.IntegerField()
	fecha_nacimiento = models.DateField()
	posicion = models.CharField(max_length=50)
	equipo_jugador = models.ForeignKey(Equipo)
	puntos_jugador = models.IntegerField(default=0)
	valor_jugador = models.IntegerField()
	goles_jugador = models.IntegerField(default=0)
	class Meta:
		model = Jugador
		fields = ['nombre_jugador', 'ciudad_natal', 'edad_jugador', 'fecha_nacimiento', 'posicion', 'equipo_jugador', 'puntos_jugador', 'valor_jugador', 'goles_jugador']

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