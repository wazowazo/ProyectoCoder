from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):

    curso_a = Curso(nombre = 'Python', camada = '27615')
    curso_a.save()

    documento = f'Tu curso es {curso_a.nombre} y tu camada es {curso_a.camada}'

    return HttpResponse(documento)