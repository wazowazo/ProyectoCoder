from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'Curso: {self.nombre} - Numero de camda: {self.camada}'

class Estudiante(models.Model):

    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail {self.email}'

class Profesor(models.Model):

    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    profesion = models.CharField(max_length = 30)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail {self.email} - Profesion: {self.profesion}'

class Entregable(models.Model):

    nombre = models.CharField(max_length = 30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f'Nombre alumno: {self.nombre} - Fecha de entrega: {self.fechaDeEntrega} - Estado: {self.entregado}'