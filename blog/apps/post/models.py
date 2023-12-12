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
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)
    def __str__(self):
        return self.titulo
    
    
    