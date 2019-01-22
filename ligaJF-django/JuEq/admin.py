from django.contrib import admin
from .models import Equipo, Jugador, Partido, Mercado
# Register your models here.
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Partido)
admin.site.register(Mercado)