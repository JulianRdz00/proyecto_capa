from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from libs.models import CommonInfo


class Curso(CommonInfo):
    titulo_curso = models.CharField(max_length=50)
    descripcion_curso = models.TextField()
    vigencia = models.DateTimeField(default=timezone.now)
    persona_asignada = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cursos")


class Modulos(CommonInfo):
    cursos = models.ForeignKey(to=Curso, on_delete=models.CASCADE, related_name="modulos")
    archivos = models.FileField(upload_to="archivos_subidos", max_length=20, null=True)
    

class Video(CommonInfo):
    modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(upload_to="videos", max_length=20, null=True)
    título = models.CharField(max_length=50)
    descripción = models.TextField(null=True)
    

#class Ejercitacion(CommonInfo):
    #modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Ejercitacion")
    #ejemplo = models.TextField(null=True)
