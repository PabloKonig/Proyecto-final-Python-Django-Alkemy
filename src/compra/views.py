from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def primera_prueba(request):
    return HttpResponse(content="Proyecto Final")
