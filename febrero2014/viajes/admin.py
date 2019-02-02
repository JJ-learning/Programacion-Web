from django.contrib import admin
from .models import Destino, Viaje, Ruta

# Register your models here.
admin.site.register(Viaje)
admin.site.register(Destino)
admin.site.register(Ruta)