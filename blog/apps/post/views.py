from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post, Categoria
from .forms import PostForm 
from django.contrib.auth.decorators import login_required

# Create your views here.
def ListarPost (request):
    contexto = {}
    id_categoria = request.GET.get("id", None)
    antiguedad = request.GET.get("antiguedad")
    orden= request.GET.get("orden")
    n = Post.objects.all()
    #filtro por categoria 
    if id_categoria:
        n = n.filter(categoria_post=id_categoria)
    #filtro por antiguedad
    if antiguedad == "asc":
        n = n.order_by('fecha_publicacion')
    elif antiguedad == "desc":
        n = n.order_by('-fecha_publicacion')
#filtro por orden alfabético
    if orden == "asc":
        n = n.order_by('titulo')
    elif orden == "desc":
        n = n.order_by('-titulo')

    contexto = {
        'post': n,
        'categorias': Categoria.objects.all(),
    }

    return render(request, 'post/listar.html', contexto)


def DetallePost(request, pk):
    contexto = {}
    
    n = Post.objects.get(pk = pk) #objeto en especifico
    contexto['post']= n
    
    #Borrar la noticia
    if request.method == 'POST' and 'delete_post' in request.POST:
        n.delete()
        return redirect ('post:listar')
    return render(request, 'post/detalle.html', contexto)

@login_required
def AgregarPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILE)#request files para imagenes
        if form.is_valid():
            post = form.save(commit=False)
            post.autor= request.user 
            form.save()
            return redirect('home')
    else: 
        form = PostForm()
        
    
    return render (request, 'post/AgregarPost.html', {'form':form})

def AgregarPost(request):
    form= PostForm(request.POST or None, request.FILES)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('home'))
    


