from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.
def index(request, peticion):
    try:
        solicitud = Pages.objects.get(name=peticion)
        #en vez del id lo podemos hacer tambien con el nombre pero esta mejor asi
    except Pages.DoesNotExist:
        return HttpResponse('Page Not Found')
    respuesta = 'Hola, soy ' + solicitud.name + ": " + str(solicitud.page)
    return HttpResponse(respuesta)

