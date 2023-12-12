
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    
    path('',views.ListarPost, name='listar'),
    path('detalle/<int:pk>',views.DetallePost, name='detalle'),
    path('AgregarPost', views.AgregarPost, name = 'AgregarPost'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)