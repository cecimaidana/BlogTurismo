from django.shortcuts import render
from apps.post.models import Post

def Home (request):
    #traer las ultimos post al home
    ultimos_post = Post.objects.order_by('-fecha_publicacion')[:3]
    contexto = {
        'ultimos_post': ultimos_post
    }
    return render(request, 'home.html')

def Acerca_de (request):
    return render(request, 'acerca_de.html')

def Contacto(request):
    return render(request, 'contacto.html')





