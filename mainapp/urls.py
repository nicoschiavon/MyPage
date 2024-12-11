from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("acerca/", views.acerca, name='acerca'),
    path("proyectos/", views.proyectos, name='proyectos'),
    path("controlFecha/", views.controlFecha, name='controlFecha')
]