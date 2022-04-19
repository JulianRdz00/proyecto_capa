from code import InteractiveConsole
from dataclasses import field
from pyexpat import model
from django import forms
from .models import Categoria, Comentarios
from .models import Curso
from .models import Modulos
from django.contrib.auth.forms import UsernameField


class CategoriaForm(forms.ModelForm):
    titulo = forms.CharField()
    icono = forms.ImageField()

    class Meta:
        Widget = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'icono': forms.FileInput(attrs={'class': 'form-control'}),
        }
        model = Categoria
        exclude = [
            'autor',
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]


class CursoForm(forms.ModelForm):
    categoria = forms.CharField()
    titulo = forms.CharField()
    descripcion = forms.Textarea()
    vigencia = forms.DateField()
    persona_asignada = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    
    class Meta:
        Widget = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'vigencia': forms.DateInput(attrs={'class': 'form-control'}),
            'persona_asignada': forms.TextInput(attrs={'class': 'form-control'}),
        }
        model = Curso
        exclude = [
            'autor',
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]
    


class ModulosForm(forms.ModelForm):
    curso = forms.CharField()
    titulo = forms.CharField()
    video = forms.FileField()
    descripcion = forms.CharField()
    archivos = forms.FileField()
    descripcion_archivos = forms.CharField()
    links_relevantes = forms.CharField()
    habilitar_chat = forms.CheckboxInput()
    habilitar_comentarios = forms.CheckboxInput()

    class Meta:
        Widget = {
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'archivos': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion_archivos': forms.Textarea(attrs={'class': 'form-control'}),
            'links_relevantes': forms.TextInput(attrs={'class': 'form-control'}),
            'habilitar_chat': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'habilitar_comentarios': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        model = Modulos
        exclude = [
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
        ]
        


class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        exclude = [
            'autor',
            'fecha_de_creación',
            'fecha_de_publicación',
            'is_deleted',
            'modulo',
        ]

