from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from shortcut.models import Shortcut, busqueda, UserProfile
from django.forms import ModelForm


class ShortcutForm(ModelForm):
	content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'shortcutText'})) 

	def is_valid(self):
		form = super(ShortcutForm, self).is_valid()
		for f in self.errors.iterkeys():
			if f!= '__all__':
				self.fields[f].widget.attrs.update({'class error shortcutText'})
		return form
	class Meta:
		model = Shortcut
		exclude = ('user',)

class search(ModelForm):
	class Meta:
		model = busqueda
		fields = ['busqueda']

	def __init__(self, *args, **kwargs):
		super(search, self).__init__(*args, **kwargs)
		self.fields['busqueda'].label = "Busqueda"

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Name'}))
	username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'User'}))
	password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
	class Meta:
		model = User
		fields = ['email', 'username', 'first_name', 'password1', 'password2']
		

	def is_valid(self):
		form = super(SignUpForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all_':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form
 
	

class AuthForm(AuthenticationForm):
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'User'}))
	password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
 
	def is_valid(self):
		form = super(AuthForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

class SettingsForm(ModelForm):
	email = forms.EmailField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Name'}))
	username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'User'}))
	password1 = forms.CharField(required=False, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(required=False, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
	class Meta:
		fields = ['email', 'username', 'first_name', 'password1', 'password2']
		model = User

	def is_valid(self):
		form = super(SettingsForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all_':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

class SettingsProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['bio', 'avatar']	
		widgets = {
			'bio': forms.Textarea(attrs= {'placeholder': 'Escribe algo sobre ti. Tienes 160 caracteres.'})	
		}

	def __init__(self, *args, **kwargs):
		super(SettingsProfileForm, self).__init__(*args, **kwargs)
		self.fields['bio'].label = "Bio"
		self.fields['avatar'].label = "avatar"

	def save(self, commit=True):
		user = super(SettingsProfileForm, self).save(commit=False)
		if commit:
			user.save()
		return user