from django import forms

class CursoFormularios(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class ProfesorFormularios(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
