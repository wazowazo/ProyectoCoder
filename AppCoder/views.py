from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormularios, ProfesorFormularios
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy






def curso(self):

    curso_a = Curso(nombre = 'Python', camada = '27615')
    curso_a.save()

    documento = f'Tu curso es {curso_a.nombre} y tu camada es {curso_a.camada}'

    return HttpResponse(documento)

def inicio(request):

    return render(request,'AppCoder/inicio.html')

""" def cursos(request):

    return render(request,'AppCoder/cursos.html') """

""" def profesores(request):

    return render(request,'AppCoder/profesores.html') """


def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormularios(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:  

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= ProfesorFormularios()

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def estudiantes(request):

    return render(request,'AppCoder/estudiantes.html')

def entregables(request):

    return render(request,'AppCoder/entregables.html')

def cursos(request):

    if request.method == 'POST':

        miFormulario = CursoFormularios(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            curso_a = Curso(nombre = informacion['curso'], camada = informacion['camada'])
            
            curso_a.save()
            
            return render(request, 'AppCoder/inicio.html')
    else:
        
        miFormulario = CursoFormularios()

    return render(request, 'AppCoder/cursos.html', {'miFormulario':miFormulario})

""" def profesorFormularios(request):
    
    if request.method == 'POST':

        miFormulario = ProfesorFormularios(request.POST)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor( nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])

            profesor.save()

            return render(request, 'AppCoder/inicio.html')
    else:

        miFormulario = ProfesorFormularios()

    return render(request, 'AppCoder/profesorFormularios.html', {'miFormulario':miFormulario}) """

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__iexact=camada)
        #respuesta = f"Estoy buscando la camada numero: { request.GET['camada'] }"
    
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})

    else:

        respuesta = "No enviaste datos"
        
    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

def leerProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {'profesores':profesores}

    return render(request, 'AppCoder/leerProfesores.html', contexto)

def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)

def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormularios(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormularios(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesores.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})


class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"


class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"


class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"