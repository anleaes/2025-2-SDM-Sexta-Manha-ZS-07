from django.db import models

# Create your models here.

class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

   
