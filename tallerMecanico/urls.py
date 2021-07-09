from django.contrib import admin
from django.urls import path, include
from .views import index, trabajos, registrarse, iniciarSesion, mantencion1, mantencion2, mantencion3, mantencion4, mantencion5, mantencion6, repuestos

urlpatterns = [
    path('', index, name="INDEX"),
    path('trabajos/', trabajos, name="TRABAJOS"),
    path('registrarse/', registrarse, name="REGISTRO"),
    path('iniciarSesion/', iniciarSesion, name="INICIAR"),
    path('mantencion1/', mantencion1, name="MANTENCION1"),
    path('mantencion2/', mantencion2, name="MANTENCION2"),
    path('mantencion3/', mantencion3, name="MANTENCION3"),
    path('mantencion4/', mantencion4, name="MANTENCION4"),
    path('mantencion5/', mantencion5, name="MANTENCION5"),
    path('mantencion6/', mantencion6, name="MANTENCION6"),
    path('repuestos/', repuestos, name="REPU"),
]
