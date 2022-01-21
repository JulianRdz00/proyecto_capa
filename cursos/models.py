from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    titulo_curso = models.CharField(max_length=50)
    descripcion_curso = models.TextField()
    vigencia = models.DateTimeField(default=timezone.now)
    persona_asignada = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name= "Persona asignada")


class Modulos(models.Model):
    cursos = models.ForeignKey(to=Curso, on_delete=models.CASCADE, related_name= "Modulos")
    archivos = models.FileField(upload_to="archivos_subidos", max_length=20, null=True)
    

class Video(models.Model):
    modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Video")
    video = models.FileField(upload_to="videos", max_length=20, null=True)
    título = models.CharField(max_length=50)
    descripción = models.TextField(null=True)
    

#class Ejercitacion(models.Model):
    #modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Ejercitacion")
    #ejemplo = models.TextField(null=True)


class CommonInfo(models.Model):
    fecha_de_creación = models.DateTimeField(default=timezone.now)
    fecha_de_publicación = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BoleanField(default=False)


    class Meta:
        abstract = True