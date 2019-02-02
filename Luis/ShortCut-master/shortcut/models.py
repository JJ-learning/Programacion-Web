from django.db import models
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage

# Create your models here.



class Shortcut(models.Model):
	content=models.CharField(max_length=140)
	creation_date=models.DateTimeField(auto_now=True, blank=True)
	user=models.ForeignKey(User)


class UserProfile(models.Model):
	user=models.OneToOneField(User)
	follows=models.ManyToManyField('self', related_name="followed_by", symmetrical=False)
	avatar = models.ImageField(upload_to='photos', blank=True)
	bio = models.CharField(max_length = 160, blank=True, default="")


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class busqueda(models.Model):
	busqueda = models.CharField(max_length = 50)

