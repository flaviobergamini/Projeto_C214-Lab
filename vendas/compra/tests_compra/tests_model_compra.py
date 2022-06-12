from django.test import TestCase

from cliente.models import Cliente
from compra.models import Compra
from produto.models import Produto

# Create your tests here.



class TestModelCompras(TestCase):

    # Função responsável por inicializar os testes (Inicializado antes de rodar os outros testes)
    def setUp(self):
        self.cliente=Cliente.objects.create(
            cpf='100.000.000-90',
            nome='Rodrigo de Freitas',
            cep='37540-000',
            email='rodrigao_frei28@hotmail.com',
            senha='rodrigao_o_mais_brabo',
            telefone='35 9.9070-8090'
        )

        self.produto=Produto.objects.create(
            idProduto=1,
            nome='Parafusadeira',
            marca='Bosch',
            preco=175.99,
            quantidade=100
        )

        self.compra=Compra.objects.create(
            idCompra=1,
            preco=self.produto.preco,
            tipoPagamento='boleto',
            codigoRastreamento='BR099089AM',
            quantidadeCoprada=25,
            cliente_cpf=self.cliente,
            produto_id=self.produto

        )

    ## TESTES UNITÁRIOS ##
    def test_str_compra_tipo_pagamento(self):
        self.assertEqual('boleto',str(self.compra.tipoPagamento))

    def test_total_compra(self):
        self.assertEqual(4179.7625,round(self.compra.calcula_total(),4))

    ## Testes de integração ##


    def test_istancia_produto_id(self):
        self.assertIsInstance(self.compra.produto_id,Produto)

    def test_istancia_cliente_cpf(self):
        self.assertIsInstance(self.compra.cliente_cpf, Cliente)

