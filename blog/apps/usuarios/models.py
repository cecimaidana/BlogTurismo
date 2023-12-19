from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios', default='default-user.png')


    USUARIO_COLABORADOR = 'Colaborador'
    USUARIO_VISITANTE = 'Visitante'
    USUARIO_MIEMBRO = 'Miembro'
    USUARIO_SUPER = 'Superusuario'
    
    
    TIPOS_DE_USUARIO = [
        (USUARIO_COLABORADOR, 'Colaborador'), 
        (USUARIO_VISITANTE, 'Visitante'), #no esta registrado, no esta logueado / no aparece en la base de datos
        (USUARIO_MIEMBRO, 'Miembro'), 
        (USUARIO_SUPER, 'Superusuario'), 
    ]
    
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO, default=USUARIO_MIEMBRO)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=Usuario)
def asignar_tipo_usuario(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.tipo_usuario = Usuario.USUARIO_SUPER
        instance.save()
        print(f"Usuario {instance.username} es un Superusuario.")
        
@receiver(post_save, sender=Usuario)
def asignar_miembro(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.tipo_usuario = Usuario.USUARIO_MIEMBRO
        instance.save()
        print(f"Usuario {instance.username} es un Miembro.")
    
    
