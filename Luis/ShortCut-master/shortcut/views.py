from django.shortcuts import render

from shortcut.models import Shortcut, UserProfile
from shortcut.forms import ShortcutForm, search, SignUpForm, AuthForm, SettingsForm, SettingsProfileForm

from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


def home(request, auth_form=None, user_form=None):
	if request.user.is_authenticated():
		sc_form = ShortcutForm()
		user = request.user
		sc_self = Shortcut.objects.filter(user=user.id).order_by('-id')
		sc_follows = Shortcut.objects.filter(user__userprofile__in=user.profile.follows.all).order_by('-id')
		shortcuts = sc_self | sc_follows
		search_form = search()

		return render(request, 'shortcut/follows.html', {'sc_form': sc_form, 'user_log': user, 'shortcuts':shortcuts, 'next_url': '/', 'search_form' :search_form, })

	else:
		auth_form = auth_form or AuthForm()
		user_form = user_form or SignUpForm()

		return render(request, 'shortcut/home.html', {'auth_form': auth_form, 'user_form': user_form, })


def newUser(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method=='POST':
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = SignUpForm()
	return render(request, 'shortcut/register.html', {'form':form, })

def login_view(request):
	if not request.user.is_anonymous(): #para saber si tiene iniciada sesion o no
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AuthForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user =  authenticate(username=username, password=password)
			if not user is None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('shortcut/banned.html', context_instance=RequestContext(request))
			else:
				return render_to_response('shortcut/not_exist.html', context_instance=RequestContext(request))
	else:
		form = AuthForm()
	return render(request, 'shortcut/login.html', {'form':form, })

@login_required(login_url = '/login')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url = '/login')
def submit(request):
	if request.method == 'POST':
		sc_form = ShortcutForm(data=request.POST)
		next_url = request.POST.get("next_url")
		if sc_form.is_valid():
			shortcut = sc_form.save(commit=False)
			shortcut.user = request.user
			shortcut.save()
			return HttpResponseRedirect(next_url)
		else:
			return public(request, sc_form)
	return HttpResponseRedirect('/')

@login_required(login_url = '/login')
def public(request, sc_form=None):
	sc_form = sc_form or ShortcutForm()
	shortcuts = Shortcut.objects.order_by('-id')[:10]
	return render(request, 'shortcut/public.html', {'sc_form':sc_form, 'next_url': '/shortcuts', 'shortcuts': shortcuts, 'user_log':request.user, })

def get_lastest(user):
	try:
		return user.shortcut_set.order_by('-id')[0]
	except IndexError:
		return ""

@login_required(login_url = '/login')
def users(request, username="", sc_form=None):
	if username:
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise Http404
		shortcuts = Shortcut.objects.filter(user=user.id).order_by('-id')
		user_log = request.user
		if username == request.user.username or request.user.profile.follows.filter(user__username=username):
			return render(request, 'shortcut/user.html', {'user': user, 'shortcuts': shortcuts, 'user_log': user_log, })
		return render(request, 'shortcut/user.html', {'user': user, 'shortcuts': shortcuts, 'follow': True, 'user_log': user_log, })
	users = User.objects.all().annotate(shortcut_count=Count('shortcut'))
	shortcuts = map(get_lastest, users)
	obj = zip(users, shortcuts)
	sc_form = sc_form or ShortcutForm()
	return render(request, 'shortcut/profiles.html', {'obj': obj, 'next_url': '/users', 'sc_form':sc_form, 'user_log': request.user, })


@login_required(login_url = '/login')
def follow(request):
	if request.method == 'POST':
		follow_id = request.POST.get('follow', False)
		if follow_id:
			try:
				user = User.objects.get(id=follow_id)
				request.user.profile.follows.add(user.profile)
			except ObjectDoesNotExist:
				return HttpResponseRedirect('/users')
	return HttpResponseRedirect('/users')

@login_required(login_url = '/login')
def interactions(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	user_log = request.user
	sc = Shortcut.objects.filter(content__icontains = user_log.username).order_by('-id')
	return render(request, 'shortcut/interactions.html', {'user_log': user_log, 'shortcuts': sc, })

@login_required(login_url = '/login')
def search_view(request, sc_form=None):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.GET.has_key('busqueda'):
		users = User.objects.filter(username__icontains=request.GET['busqueda']).annotate(shortcut_count=Count('shortcut'))
		sc = Shortcut.objects.filter(content__icontains = request.GET['busqueda']).order_by('-id')
		sc_form = ShortcutForm()
		return render_to_response('shortcut/search.html',
		{
			'user_log' : request.user,
			'users' : users,
			'shortcuts' : sc,
			'busqueda' : request.GET['busqueda'],
			'sc_form' : sc_form,
			
		}, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('shortcut.views.home'))

@login_required(login_url = '/login')
def settings(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	u = request.user
	if request.method == 'POST':
		form = SettingsForm(request.POST, request.FILES, instance=u)
		form_p = SettingsProfileForm(request.POST, request.FILES, instance=u)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('shortcut.views.settings'))
		if form_p.is_valid():
			form_p.save()
			return HttpResponseRedirect(reverse('shortcut.views.settings'))
	else:
		form = SettingsForm(instance=u)
		form_p = SettingsProfileForm(instance=u)
	
	return render(request, 'shortcut/settings.html', {'user_log': u, 'form': form, 'form_p': form_p})
	


