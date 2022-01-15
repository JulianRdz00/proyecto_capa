from django.utils import timezone
from django.db import models

class Modulos(models.Model):
    archivos = models.FileField(upload_to="archivos_subidos", max_length=20, null=True)
    fecha_de_creación = models.DateTimeField(default=timezone.now)
    fecha_de_publicación = models.DateTimeField(blank=True, null=True)


class Video(models.Model):
    modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Video")
    video = models.FileField(upload_to="videos", max_length=20, null=True)
    título = models.CharField(max_length=50)
    descripción = models.TextField(null=True)
    

class Ejercitación(models.Model):
    modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Ejercitación")
    ejemplo = models.TextField(null=True)

# Create your models here.
