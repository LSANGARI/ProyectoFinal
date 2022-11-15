from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Autor
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_autor(sender,instance, created, **kwargs):
    if created:
        Autor.objects.create(username=instance, nombre=instance.first_name, apellido=instance.last_name, correo=instance.email)
        