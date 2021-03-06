from django.urls import path
from .import views


urlpatterns = [
    path('', views.perfil_lista, name='perfil_lista'),
    path('perfil/<int:pk>/', views.perfil_detalle, name='perfil_detalle'),
    path('perfil/<int:pk>/editar/', views.perfil_editar, name='perfil_editar'),
    path('nuevo_perfil', views.perfil_nuevo, name='perfil_nuevo'),
]