
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    
    path('',views.ListarPost, name='listar'),
    path('detalle/<int:pk>',views.DetallePost, name='detalle'),
    path('addPost', views.AddPost, name = 'addpost'),
    path('post/<int:pk>/edit/', views.EditarPost, name='edit_post'),

    path('comentario/add/<int:post_id>', views.AddComentario, name='add_comentario'),
    path('comentario/delete/<int:comentario_id>', views.BorrarComentario, name='delete_comentario'),
    path('comentario/edit/<int:comentario_id>', views.EditarComentario, name='edit_comentario'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)