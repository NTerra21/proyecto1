from django.shortcuts import render
from app1.forms import AlumnoForm, ProfesorForm, CursoForm
from app1.models import Estudiantes, Curso, Profesor


def inicio(request):
    return render(request, "inicio.html")


def estudiantes(request):

    if request.method == 'POST':

        miFormulario = AlumnoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            estudiante = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])

            estudiante.save()

            return render(request, "estudiantes.html")

    else:

        miFormulario = AlumnoForm()

    return render(request, "estudiantes.html", {"miFormulario": miFormulario})



def profesor(request):

        if request.method == 'POST':

            miFormulario = ProfesorForm(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion'])

                  profesor.save()

                  return render(request, "profesores.html")
        else:

            miFormulario= ProfesorForm() #Formulario vacio para construir el html

        return render(request, "profesores.html", {"miFormulario":miFormulario})




def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoForm(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['comision'])

                  curso.save()

                  return render(request, "curso.html") #Vuelvo al inicio o a donde quieran

      else:

            miFormulario= CursoForm() #Formulario vacio para construir el html

      return render(request, "curso.html", {"miFormulario":miFormulario})


