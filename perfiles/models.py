from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField


genero_opciones = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('Otro','Otro'),
)

conocimientos_ingles = (
        ('Basico','Basico'),
        ('Intermedio','Intermedio'),
        ('Avanzado','Avanzado'),
)


class Perfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ingles = models.CharField(
        max_length=12,
        choices= conocimientos_ingles,
        default='Nulo',
        blank=True,
        null=True,
        )
    formacion_academica = models.TextField(max_length=500, null=True, blank=True)
    profesion = models.TextField(max_length=100, null=True, blank=True)
    fotos = models.ImageField(upload_to="fotos", null=True, blank=True)
    webPage = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    nacionalidad = CountryField(null=True, blank=True)
    genero = models.CharField(
        max_length=12,
        choices= genero_opciones,
        default='Nulo',
        null=True,
        blank=True,
        )