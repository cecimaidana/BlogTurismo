from django import forms 
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = [
            'titulo'
            'resumen'
            'contenido',
            'imagenes',
            'categoria_post',
        ]
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario 
        fields = [
            'contenido'
        ]
        exclude = ['usuario']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        
        super(ComentarioForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario = user.username