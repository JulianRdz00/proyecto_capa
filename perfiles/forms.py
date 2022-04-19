from django import forms
from .models import Perfiles
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _

class FormPerfiles(forms.ModelForm):

    class Meta:
        model = Perfiles
        fields = ('user', 'formacion_academica', 'profesion', 'fotos', 'webPage', 'twitter', 'facebook', 'linkedin', 'youtube', 'nacionalidad', 'genero', 'ingles')


class UserloginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    class Meta:
        widget = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }