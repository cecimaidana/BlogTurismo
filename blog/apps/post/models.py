from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Post (models.Model):
    titulo = models.CharField(max_length=50) #VARCHAR 
    resumen = models.CharField(max_length=200, null=True)
    contenido = models.TextField()
    #libreria pillow
    imagenes = models.ImageField(upload_to='post')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria_post = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    #autor = models.ForeignKey(Usuario, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.contenido
    
    