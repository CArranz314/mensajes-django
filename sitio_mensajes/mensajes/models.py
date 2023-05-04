from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mensaje(models.Model):
    """
    Modelo para la tabla de mensajes
    """

    usuario = models.ForeignKey(User, related_name="mensaje", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, blank=True)
    contenido = models.TextField()
    fecha = models.DateTimeField()
