from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app1.forms import AlumnoFormulario
from app1.models import Estudiantes


def estudiantes(request):

    if request.method == 'POST':

        miFormulario = AlumnoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            estudiante = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])

            estudiante.save()

            return render(request, "estudiantes.html")

    else:

        miFormulario = AlumnoFormulario()

    return render(request, "estudiantes.html", {"miFormulario": miFormulario})


def inicio(request):
    return render(request, "inicio.html")


def profesor(request):
    return render(request, 'profesores.html')