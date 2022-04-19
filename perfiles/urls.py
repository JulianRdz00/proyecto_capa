from django.urls import path
from .import views


urlpatterns = [
    path('perfiles/', views.perfil_lista, name='perfil_lista'),
    path('perfil/<int:pk>/', views.perfil_detalle, name='perfil_detalle'),
    path('perfil/<int:pk>/editar/', views.perfil_editar, name='perfil_editar'),
    path('nuevo_perfil/', views.perfil_nuevo, name='perfil_nuevo'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]