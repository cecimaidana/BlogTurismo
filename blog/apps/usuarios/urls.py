
from django.urls import path
from . import views
app_name = 'usuarios'

urlpatterns = [
    
    path('login/', views.user_login, name = 'login'),#vista basada en funciones
    path('logout/',views.user_logout, name= 'logout'),
    path('registro/',views.Registro.as_view(), name='registro'),#vista basada en clases
]