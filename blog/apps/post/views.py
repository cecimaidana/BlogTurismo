from django.shortcuts import render
from .models import Post
# Create your views here.
def ListarPost (request):
    contexto = {}
    
    n = Post.objects.all() #select * from post
    contexto['post']= n
    return render (request, 'post/listar.html', contexto)
