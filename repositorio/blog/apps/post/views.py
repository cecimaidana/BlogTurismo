from django.shortcuts import render

# Create your views here.
def ListarPost (request):
    return render (request, 'post/listar.html')
