from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('administrador/', views.administrador, name='administrador'),
    path('editar_contrasenia/<int:pk>/', views.editar, name='editar_contrasenia'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),
]