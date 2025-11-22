from django.db import models

# Create your models here.
class Cliente(models.Model):
<<<<<<< HEAD
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.senha}'
=======
    name = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=100)
    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.email}"
>>>>>>> origin/main
