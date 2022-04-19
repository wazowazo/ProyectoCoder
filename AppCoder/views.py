from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader

def curso(self):

    curso_a = Curso(nombre = 'Python', camada = '27615')
    curso_a.save()

    documento = f'Tu curso es {curso_a.nombre} y tu camada es {curso_a.camada}'

    return HttpResponse(documento)

def inicio(request):

    return render(request,'AppCoder/inicio.html')

def cursos(request):

    return render(request,'AppCoder/cursos.html')

def profesores(request):

    return render(request,'AppCoder/profesores.html')

def estudiantes(request):

    return render(request,'AppCoder/estudiantes.html')

def entregables(request):

    return render(request,'AppCoder/entregables.html')