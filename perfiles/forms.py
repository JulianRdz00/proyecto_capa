from django import forms
from .models import Perfiles


class FormPerfiles(forms.ModelForm):

    class Meta:
        model = Perfiles
        fields = ('user', 'formacion_academica', 'profesion', 'fotos', 'webPage', 'twitter', 'facebook', 'linkedin', 'youtube', 'nacionalidad', 'genero', 'ingles')
