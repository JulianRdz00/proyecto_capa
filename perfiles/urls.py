from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Perfiles/edit', views.perfil_edit, name='perfil_edit')
]