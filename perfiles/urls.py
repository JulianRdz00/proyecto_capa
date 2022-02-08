from django.urls import path
from . import views


urlpatterns = [
    path('', views.perfil_list, name='perfil_list'),
    path('post/<int:pk>/', views.perfil_detail, name='perfil_detail'),
    path('post/<int:pk>/edit/', views.perfil_edit, name='perfil_edit'),
    path('Perfiles/new', views.perfil_new, name='perfil_new'),
]