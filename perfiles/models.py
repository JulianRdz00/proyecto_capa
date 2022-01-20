from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Perfiles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	# pais = models.TextField(max_length=50) (fijarse si hay alguna forma de seleccionar pais)
    # genero = models.TextField(max_length=50) (fijarse si hay alguna forma de configurar opciones a seleccionar)
    # conocimientos_ingles = models.TextField(max_length=50) (fijarse si hay alguna forma de configurar opciones a seleccionar)
    formacion_academica = models.TextField(max_length=500, null= True)
    profesion = models.TextField(max_length=100, null= True)
    fotos = models.ImageField(upload_to="fotos", null=True)
    webPage = models.CharField(max_length=100, null= True)
    twitter = models.CharField(max_length=100, null= True)
    facebook = models.CharField(max_length=100, null= True)
    linkedin = models.CharField(max_length=100, null= True)
    youtube = models.CharField(max_length=100, null= True)