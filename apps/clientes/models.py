from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=100)
