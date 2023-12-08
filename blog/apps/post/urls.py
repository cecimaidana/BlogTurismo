
from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    
    path('',views.ListarPost, name='listar'),
    path('detalle/<int:pk>',views.DetallePost, name='detalle'),
    
]