from dataclasses import field
from pyexpat import model
from django import forms
from .models import Categoria
from .models import Curso
from .models import Modulos


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = [
            'autor',
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]


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
