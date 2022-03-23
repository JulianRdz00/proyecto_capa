from django.urls import path
from . import views


urlpatterns = [
    path('curso/<int:pk>/modulo/<int:pk_modulo>/categoria/<int:pk_categoria>/', views.curso_showtime, name='curso_vista'),
    path('curso/crear/', views.nuevo_curso, name='nuevo_curso'),
    path('curso/<int:pk>/detalle/', views.detalle_curso, name='detalle_curso'),
    path('curso/<int:pk>/editar/', views.editar_curso, name='editar_curso'),
    path('modulo/crear/', views.nuevo_modulo, name='nuevo_modulo'),
    path('modulo/<int:pk>/detalle/', views.detalle_modulo, name='detalle_modulo'),
    path('modulo/<int:pk>/editar/', views.editar_modulo, name='editar_modulo'),
    path('categoria/crear/', views.nueva_categoria, name='nueva_categoria'),
    path('categoria/<int:pk>/detalle/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('curso/<int:pk>/modulo/<int:pk_modulo>/categoria/<int:pk_categoria>/video/', views.curso_video, name='curso_video'),
    path('curso/<int:pk>/modulo/<int:pk_modulo>/categoria/<int:pk_categoria>/descripcion/', views.curso_descripcion, name='curso_descripcion'),
    path('comentario/crear/', views.nuevo_comentario, name='nuevo_comentario'),
    path('comentario/<int:pk>/detalle/', views.detalle_comentario, name='detalle_comentario'),
    path('comentario/<int:pk>/editar/', views.editar_comentario, name='editar_comentario'),
]
