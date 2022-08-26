from django.urls import path
from app1.views import  profesor,inicio, estudiantes, cursos, buscar


urlpatterns = [
    path("profesor/", profesor, name='app1Profesor'),
    path("estudiantes/", estudiantes, name='app1Estudiantes'),
    path("curso/", cursos, name='app1Cursos'),
    path("buscar/", buscar),
    path("", inicio, name= 'app1Inicio'),
]