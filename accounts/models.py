from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.secretarias.models import Secretaria


# Atributos customizados devem ser adicionados aqui
class CustomUser(AbstractUser):
    secretarias = models.ManyToManyField(Secretaria, blank=True, related_name='usuarios_secretarias')
