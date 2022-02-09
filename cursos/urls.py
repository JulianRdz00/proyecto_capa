from django.urls import path
from . import views

urlpatterns = [
    path('curso/crear/', views.nuevo_curso, name='nuevo_curso'),
    path('modulo/crear/', views.nuevo_modulo, name='nuevo_modulo'),
    path('video/subir/', views.nuevo_video, name='nuevo_video'),
    path('curso/<int:pk>/detalle/', views.detalle_curso, name='detalle_curso'),
    path('curso/<int:pk>/editar/', views.editar_curso, name='editar_curso'),
    path('modulo/<int:pk>/detalle/', views.detalle_modulo, name='detalle_modulo'),
    path('modulo/<int:pk>/editar/', views.editar_modulo, name='editar_modulo'),
    path('video/<int:pk>/detalle/', views.detalle_video, name='detalle_video'),
    path('video/<int:pk>/editar/', views.editar_video, name='editar_video'),
]
