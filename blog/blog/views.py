from django.shortcuts import render
from apps.post.models import Post

def Home (request):
    ultimos_post = Post.objects.order_by('-fecha_publicacion')[:4]
    contexto = {
        'ultimos_post': ultimos_post
    }
    #traer las ultimos post al home
    return render(request, 'home.html', contexto)

def Acerca_de (request):
    return render(request, 'acerca_de.html')

def Contacto(request):
    return render(request, 'contacto/contacto.html')







