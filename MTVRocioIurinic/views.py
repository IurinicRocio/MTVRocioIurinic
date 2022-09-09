from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from Familiares.models import Padres, Familiar

def padres(request):

    plantilla = loader.get_template('padres.html') 
    
    padres = Padres.objects.all()
    contexto = {'padres': padres}

    return HttpResponse(plantilla.render(contexto))

def familiares(request):

    plantilla = loader.get_template('familiares.html') 
    
    familiares = Familiar.objects.all()
    contexto = {'familiares': familiares}

    return HttpResponse(plantilla.render(contexto))