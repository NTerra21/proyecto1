from django import forms


class CursoForm(forms.Form):

    curso = forms.CharField()
    comision = forms.IntegerField()


class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class AlumnoForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

