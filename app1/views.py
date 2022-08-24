from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def profesor(request):


    prof = {
        "profe1": {
            "profe0":"profe",
            "profe2": "profe2"}
    }

    plantilla = loader.get_template("Profesor.html")
    documento_texto = plantilla.render(prof)

    return HttpResponse(documento_texto)


def alumno(request):
    return render(request, "index.html")