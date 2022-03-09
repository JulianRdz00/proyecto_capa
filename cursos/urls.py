from django.urls import path
from . import views


urlpatterns = [
    path('curso/<int:pk>/modulo/<int:pk_modulo>/', views.curso_showtime, name='curso_vista'),
    path('curso/crear/', views.nuevo_curso, name='nuevo_curso'),
    path('curso/<int:pk>/detalle/', views.detalle_curso, name='detalle_curso'),
    path('curso/<int:pk>/editar/', views.editar_curso, name='editar_curso'),
    path('modulo/crear/', views.nuevo_modulo, name='nuevo_modulo'),
    path('modulo/<int:pk>/detalle/', views.detalle_modulo, name='detalle_modulo'),
    path('modulo/<int:pk>/editar/', views.editar_modulo, name='editar_modulo'),
    path('categoria/crear/', views.nueva_categoria, name='nueva_categoria'),
    path('categoria/<int:pk>/detalle/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('curso/<int:pk>/modulo/<int:pk_modulo>/video', views.curso_video, name='curso_video'),
]
