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

    # Metódos da classe
    def __calcula_total_desconto(self):
        """
        As seguintes condições devem ser respeitada as seguintes regras
        para a precificação do produto:

        - Caso seja comprado a unidade, o preço deve ser mantido como anteriormente precificado

        - Caso seja uma quantidade que esteja, 10<=qtd <=99 é concedido ao cliente um total de 5% de desconto

        - Caso seja comprado a centena é concedido ao cliente um total de 15% de desconto
      """

        if (self.quantidadeCoprada >= 10 and self.quantidadeCoprada <= 99):
            self.preco=self.preco - (self.preco * 0.05)
            return self.quantidadeCoprada*self.preco;

        if (self.quantidadeCoprada >= 100):
            self.preco = self.preco - (self.preco * 0.15)
            return self.quantidadeCoprada * self.preco;

    def calcula_total(self):

        return self.__calcula_total_desconto();