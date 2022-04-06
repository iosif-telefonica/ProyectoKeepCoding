from django.shortcuts import render
from django.http import HttpResponse
from AppKeepCoding.models import Curso, Estudiante, Profesor, Entregable
from datetime import datetime
# Create your views here.

def curso(self):
    curso = Curso(nombre = "SQL", camada = "15847")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre}, <br>camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def estudiante(self):
    estudiante = Estudiante(nombre = "Losif", apellido = "KeepCoding", email = "losif@telefonica.com")
    estudiante.save()
    documentoDeTexto = f"Nombre: {estudiante.nombre}, <br>apellido: {estudiante.apellido}, <br>email: {estudiante.email}"
    return HttpResponse(documentoDeTexto)

def profesor(self):
    profesor = Profesor(nombre = "Juancho", apellido = "Telefonica", email = "juanf@telefonica.com", profesion = "jubilado")
    profesor.save()
    documentoDeTexto = f"Nombre del Profesor: {profesor.nombre}, <br>apellido: {profesor.apellido}, <br>email: {profesor.email}, <br>profesion: {profesor.profesion}"
    return HttpResponse(documentoDeTexto)


def entregable(self):
    entregable = Entregable(nombre = "Proyecto", fechaDeEntrega = datetime.now() , entregado = True)
    entregable.save()
    documentoDeTexto = f"Entregable: {entregable.nombre}, <br>Fecha de entrega: {entregable.fechaDeEntrega}, <br>Entregado: {entregable.entregado}"
    return HttpResponse(documentoDeTexto)
