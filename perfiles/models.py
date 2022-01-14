from django.conf import settings
from django.db import models
from django.utils import timezone

class Perfiles(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
	# pais = models.TextField(max_length=50) (fijarse si hay alguna forma de seleccionar pais)
    # genero = models.TextField(max_length=50) (fijarse si hay alguna forma de configurar opciones a seleccionar)
    # conocimientos_ingles = models.TextField(max_length=50) (fijarse si hay alguna forma de configurar opciones a seleccionar)
    formacion_academica = models.TextField(max_length=500)
    profesion = models.TextField(max_length=100)
    fotos = models.ImageField(upload_to="fotos", null=True)
    webPage = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    biografia = models.CharField(max_length=500)
    nacimiento = models.DateField(
		default=timezone.now, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title