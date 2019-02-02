from django.shortcuts import render, HttpResponse, loader,get_object_or_404, redirect
from django.template import RequestContext
from .models import Destino, Viaje
from viajes.forms import DestinoForm, ViajeForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

# Create your views here.

def destinos(request):
	lista_destinos = Destino.objects.order_by('pais')
	template = loader.get_template('viajes/destinos.html')
	context={
		'lista_destinos':lista_destinos,
	}
	return HttpResponse(template.render(context, request))

def destino(request, destino_id):
	destino=get_object_or_404(Destino, id=destino_id)
	template=loader.get_template('viajes/destino.html')
	context={
		'destino':destino,
	}
	return HttpResponse(template.render(context, request))

def newD(request):
	if request.method=="POST":
		form = DestinoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/')
	else:
		form=DestinoForm()
	context={
		'form':form,
	}
	template=loader.get_template('viajes/newD.html')
	return HttpResponse(template.render(context, request))

def viajes(request):
	lista_viajes = Viaje.objects.order_by('coste_viaje')
	context={
		'lista_viajes':lista_viajes,
	}
	template = loader.get_template('viajes/Tviajes.html')
	return HttpResponse(template.render(context, request))

def newV(request):
	if request.method=="POST":
		form = ViajeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/')
	else:
		form=ViajeForm()
	context={
		'form':form,
	}
	template=loader.get_template('viajes/newV.html')
	return HttpResponse(template.render(context, request))

def viaje(request, viaje_id):
	viaje=get_object_or_404(Viaje, id=viaje_id)
	template=loader.get_template('viajes/viaje.html')
	context={
		'viaje':viaje,
	}	
	return HttpResponse(template.render(context, request))

def editarV(request, viaje_id):
	viaje=get_object_or_404(Viaje, id=viaje_id)
	if request.method == "POST":
		form = ViajeForm(request.POST, instance=viaje)
		if form.is_valid():
			viaje = form.save(commit=False)
			viaje.save()
			return redirect('/viajes', viaje_id)
	else:
		form=ViajeForm()

	context={
		'form':form,
		'viaje':viaje,
	}
	template=loader.get_template('viajes/editarV.html')
	return HttpResponse(template.render(context,request))

def login_view(request):
	message = None
	if request.method =="POST":
		form = loginForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					message = "Login incorrecto"
			else:
				message = "Nombre y/o password incorrectos"
	else:
		form = loginForm()		
	return render(request, 'viajes/login.html', {'message':message, 'form':form})

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

class rutas(TemplateView):
	 template_name = "viajes/rutas.html"

	 def rutas(self, request):
	 	lista_rutas = Ruta.objects.order_by('nombre_ruta')
	 	context={
	 		'lista_rutas':lista_rutas,
	 	}
	 	return context

	 	