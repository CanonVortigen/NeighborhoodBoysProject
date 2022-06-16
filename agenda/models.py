from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=8)
    imagem = models.ImageField(upload_to='clientes/', blank=True, null=True)
    descricao = models.TextField(max_length=100)
    horario = models.TimeField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.nome