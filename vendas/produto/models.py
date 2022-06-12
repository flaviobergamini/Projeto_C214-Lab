from django.db import models
from uuid import uuid1


class Produto(models.Model):
    idProduto = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=20)
    preco = models.FloatField()
    quantidade = models.IntegerField(blank=True, null=True)

    def __calcula_total_desconto(self):
        """
        As seguintes condições devem ser respeitada as seguintes regras
        para a precificação do produto:

        - Caso seja comprado a unidade, o preço deve ser mantido como anteriormente precificado

        - Caso seja uma quantidade que esteja, 10<=qtd <=99 é concedido ao cliente um total de 5% de desconto

        - Caso seja comprado a centena é concedido ao cliente um total de 15% de desconto
      """

        if (self.quantidade >= 10 and self.quantidade <= 99):
            self.preco=self.preco - (self.preco * 0.05)
            return self.quantidade*self.preco;

        if (self.quantidade >= 100):
            self.preco = self.preco - (self.preco * 0.15)
            return self.quantidade * self.preco;


    def calcula_total(self):

        return self.__calcula_total_desconto();

