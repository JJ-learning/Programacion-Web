from django.shortcuts import render, HttpResponse, loader, get_object_or_404, redirect
from django.template import RequestContext
from JuEq.models import Equipo, Jugador
from JuEq.forms import JugadorForm, loginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def equipos(request, equipo_id, auth_form=None, user_form=None):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	equipo=get_object_or_404(Equipo,id = equipo_id)
	template=loader.get_template('JuEq/Equipos.html')
	datosJugador=Jugador.objects.filter(equipo_jugador=equipo)
	context={
		'equipo': equipo,
		'datosJugador':datosJugador,
		'lista_equipo': lista_equipo,
	}
	return HttpResponse(template.render(context, request))

def home(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	template = loader.get_template('JuEq/home.html')
	context={
		'lista_equipo': lista_equipo,
	}
	return HttpResponse(template.render(context, request))

def jugadores(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	lista_jugador=Jugador.objects.order_by('equipo_jugador')
	template = loader.get_template('JuEq/jugadores.html')
	context={ 'lista_jugador':lista_jugador, 'lista_equipo': lista_equipo,}
	return HttpResponse(template.render(context, request))

def jugador(request, jugador_id, auth_form=None, user_form=None):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	jugador=get_object_or_404(Jugador, id=jugador_id)
	template = loader.get_template('JuEq/jugador.html')
	context={
		'jugador':jugador,
		'lista_equipo': lista_equipo,
	}
	return HttpResponse(template.render(context, request))

def nuevoJugador(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	if request.method== "POST":
		form = JugadorForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/jugadores')
	else:
		form=JugadorForm()

	context={
		'form':form
	}
	template= loader.get_template('JuEq/crearJugador.html')
	return HttpResponse(template.render(context, request))

def borrarJugador(request, jugador_id):
	jugador=get_object_or_404(Jugador, id=jugador_id)
	jugador.delete()
	return redirect('/jugadores')
	context={

		'jugador':jugador,
	}
	template= loader.get_template('JuEq/borrarJugador.html')
	return HttpResponse(template.render(context, request))

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
	return render(request, 'JuEq/login.html', {'message':message, 'form':form})	

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def nuevoUsuario(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = SignUpForm()
	return render(request, 'JuEq/register.html', {'form':form})

def instrucciones(request):
	lista_equipo = Equipo.objects.order_by('nombre_equipo')
	context={
		'lista_equipo':lista_equipo,
	}
	template = loader.get_template('JuEq/instrucciones.html')
	return HttpResponse(template.render(context, request))