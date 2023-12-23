from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.
def ListarPost (request):
    contexto = {}
    id_categoria = request.GET.get("id", None)
    antiguedad = request.GET.get("antiguedad", None)
    orden= request.GET.get("orden", None)
    
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

#detalle post con comentarios
def DetallePost(request, pk):
    
    n = Post.objects.get(pk = pk) #objeto en especifico
    c = n.comentarios.all()
    
    
    #Borrar la noticia
    if request.method == 'POST' and 'delete_post' in request.POST:
        n.delete()
        return redirect ('post:listar')
    #agregar comentario
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            form.save()
            return redirect('post:detalle', pk=pk)
    else:
        form = ComentarioForm()
    
    contexto = {
        'post': n,
        'comentarios': c,
        'form': form,
    }
    return render(request, 'post/detalle.html', contexto)




@login_required
def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES) #files es para las imagenes       
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()  
    return render (request, 'post/addPost.html', {'form':form})



@login_required
def AddComentario(request, post_id):
    post = get_object_or_404(Post, id = post_id)   
    if request.method == 'POST':
        contenido = request.POST.get("contenido")
        usuario = request.user.username
        # crear comentario
        Comentario.objects.create(post = post, usuario = usuario, contenido = contenido)
    
    return redirect('post:detalle', pk = post_id)


@login_required
def BorrarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id = comentario_id)   
    if comentario.usuario == request.user.username:
        comentario.delete()

    return redirect('post:detalle', pk = comentario.post.pk)

@login_required
def EditarPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
        # Solo el autor puede editar la noticia
    if post.autor != request.user:
        return HttpResponseForbidden("No tenes permiso para editar esta noticia.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:detalle', pk=pk)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }
    return render(request, 'post/editar.html', context)
    
#editar comentario
@login_required
def EditarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    #if comentario.autor != request.user.username:
        #messages.error(request, 'No podes editar este comentario?)
        #return redirect('post:detalle', pk=comentario.post.pk) 
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('post:detalle', pk=comentario.post.pk)
    else:
        form = ComentarioForm(instance=comentario)
    contexto ={
        'form':form,
        'comentario': comentario,
    }
    return render(request, 'post/editar_comentario.html', contexto)
    


