from django.shortcuts import render
from .models import Post, Categoria
# Create your views here.
def ListarPost (request):
    contexto = {}
    id_categoria = request.GET.get("id", None)
    
    if id_categoria:
        n= Post.objects.filter(categoria_post = id_categoria)
    else:
        n = Post.objects.all() #todas las noticias
    
    #filtro por antiguedad ascendente
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Post.objects.all().order_by('fecha_publicacion')
        
    #filtro por antiguedad descendente
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n = Post.objects.all().order_by('-fecha_publicacion')
    
    #filtro por orden alfabetico ascendente (titulo)
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Post.objects.all().order_by('titulo')
        
    #filtro orden alfabetico descendente (titulo)
    orden_desc = request.GET.get("orden_desc")
    if orden_desc:
        n = Post.objects.all().order_by('-titulo')    
        
    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre las categorias
    contexto['post']= n
    contexto['categoria'] = cat
    
    return render (request, 'post/listar.html', contexto)

def DetallePost(request, pk):
    contexto = {}
    
    n = Post.objects.get(pk = pk) #objeto en especifico
    contexto['post']= n
    return render (request, 'post/detalle.html', contexto)


