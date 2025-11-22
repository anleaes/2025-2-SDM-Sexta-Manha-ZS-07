from django.db import models
<<<<<<< HEAD
from clientes.models import Cliente
from museus.models import Museu
# Create your models here.

class Reserva(models.Model):
    data = models.DateField()
    qtd_pessoas = models.IntegerField()
    status = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    museu = models.ForeignKey(Museu, on_delete=models.CASCADE, related_name='reservas', null=True,   # ← ADICIONE TEMPORARIAMENTE
    blank=True)
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nome} - {self.data}"
=======

# Create your models here.
class Reserva(models.Model):
    status = models.CharField(max_length=50)
    qtd_pessoas = models.IntegerField()
    data = models.DateField()
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering =['id']

    def __str__(self):
        return f"{self.status} - {self.qtd_pessoas} - {self.data}"
>>>>>>> origin/main
