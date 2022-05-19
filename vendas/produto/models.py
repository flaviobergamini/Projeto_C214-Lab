from django.db import models
from uuid import uuid4


class Produto(models.Model):
    idProduto = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=10)
    preco = models.FloatField()
    quantidade = models.IntegerField(blank=True, null=True)
    