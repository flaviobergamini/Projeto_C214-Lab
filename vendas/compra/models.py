from django.db import models
from uuid import uuid1

from cliente.models import Cliente
from produto.models import Produto

class Compra(models.Model):
    idCompra = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    preco = models.FloatField()
    tipoPagamento = models.CharField(max_length=15)
    codigoRastreamento = models.CharField(max_length=15)
    quantidadeCoprada = models.IntegerField()
    cliente_cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)