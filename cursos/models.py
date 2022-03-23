from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from libs.models import CommonInfo


class Categoria(CommonInfo):
    titulo = models.CharField(max_length=50, unique=True)
    icono = models.ImageField(upload_to="iconos", null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo

class Curso(CommonInfo):
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, related_name="cursos", null=True)
    titulo = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(null=True, blank=True)
    vigencia = models.DateTimeField(null=True, blank=True)
    persona_asignada = models.ForeignKey(null=True, blank=True, to=User, on_delete=models.CASCADE, related_name="asignado")
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cursos", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.titulo


class Modulos(CommonInfo):
    curso = models.ForeignKey(to=Curso, on_delete=models.CASCADE, related_name="modulos")
    titulo = models.CharField(max_length=50, null=True)
    video = models.FileField(upload_to="videos", max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    archivos = models.FileField(upload_to="archivos_subidos", null=True, blank=True)
    descripcion_archivos = models.TextField(null=True, blank=True)
    links_relevantes = models.TextField(null=True, blank=True)
    habilitar_chat = models.BooleanField(default=True)
    habilitar_comentarios = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.titulo


class Comentarios(CommonInfo):
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="usuario_comentarios", null=True, blank=True)
    comentario = models.TextField()
    modulo = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name="modulo_comentarios", null=True, blank=True)


#class Ejercitacion(CommonInfo):
    #modulos = models.ForeignKey(to=Modulos, on_delete=models.CASCADE, related_name= "Ejercitacion")
    #opcion_1 = models.TextField()
    #opcion_2 = models.TextField()
    #opcion_3 = models.TextField(null=True)
    #opcion_4 = models.TextField(null=True)
    #opcion_5 = models.TextField(null=True)
    #opcion_correcta = models.Texfield()
