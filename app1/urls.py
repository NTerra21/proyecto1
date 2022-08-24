from django.urls import path
from app1.views import  profesor, alumno


urlpatterns = [
    path("profesor/", profesor, name='app1Profesor'),
    path("", alumno, name= 'app1Inicio'),
]