from django.conf.urls import url
from . import views


app_name='mercado'
urlpatterns=[
	url(r'^$', views.mercado, name="mercado"),
	url(r'^comprar/$', views.comprar, name="comprar"),
]