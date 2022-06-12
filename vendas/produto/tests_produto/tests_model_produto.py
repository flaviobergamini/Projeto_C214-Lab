from django.test import TestCase
from produto.models import Produto

# Create your tests here.



class TestModelCompras(TestCase):

    # Função responsável por inicializar os testes (Inicializado antes de rodar os outros testes)
    def setUp(self):
        self.produto = Produto.objects.create(
            idProduto=1,
            nome='Parafusadeira',
            marca='Bosch',
            preco=175.99,
            quantidade=100
        )

    ## TESTES UNITÁRIOS ##
    def test_qtd_produto(self):
        self.assertEqual(100, self.produto.quantidade)

    def test_marca_produto(self):
        self.assertEqual('Bosch', str(self.produto.marca))
    ## TESTES DE INTEGRAÇÃO ##


