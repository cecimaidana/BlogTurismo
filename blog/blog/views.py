from django.shortcuts import render

def Home (request):
    return render(request, 'home.html')

def Acerca_de (request):
    return render(request, 'acerca_de.html')

def Contacto(request):
    return render(request, 'contacto.html')





