from django.shortcuts import render
from apps.post.models import Post

def Home (request):
    #traer las ultimos post al home
    return render(request, 'home.html')

def Acerca_de (request):
    return render(request, 'acerca_de.html')

def Contacto(request):
    return render(request, 'contacto/contacto.html')







