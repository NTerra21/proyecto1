from django.urls import path
from app1.views import  profesor,inicio, estudiantes


urlpatterns = [
    path("profesor/", profesor, name='app1Profesor'),
    path("estudiantes/", estudiantes, name='app1Estudiantes'),
    path("", inicio, name= 'app1Inicio'),
]