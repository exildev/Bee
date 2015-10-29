from django.db import models
from django.contrib.auth.models import User

class Desarrollador(models.Model):
	usuario = models.ForeignKey(User)
#end class

class Cliente(models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=100)
#end class


