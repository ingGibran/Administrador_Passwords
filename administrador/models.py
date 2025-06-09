from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contrasenia(models.Model):
    servicio = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    usuario_servicio = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo