from django.conf.urls import url
from . import views


app_name='CaRe'
urlpatterns=[
	url(r'^$', views.clasificacion, name="clasificacion"),
]