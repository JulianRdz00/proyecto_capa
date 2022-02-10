from dataclasses import field
from pyexpat import model
from django import forms
from .models import Curso
from .models import Modulos
from .models import Video


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = [
            'autor',
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]


class ModulosForm(forms.ModelForm):
    class Meta:
        model = Modulos
        exclude = [
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = [
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]
