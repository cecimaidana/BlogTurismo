from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Post (models.Model):
    titulo = models.CharField(max_length=50) #VARCHAR 
    contenido = models.TextField()
    #libreria pillow
    imagenes = models.ImageField(upload_to='post')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria_post = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.titulo
    
    
    