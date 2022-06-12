from django.test import TestCase
from cliente.models import Cliente

# Create your tests here.



class TestModelClient(TestCase):

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

    ## TESTES UNITÁRIOS ##

    def test_str_cliente_retornar_nome(self):
        self.assertEqual('Rodrigo de Freitas',str(self.cliente.nome))


    def test_str_cliente_retornar_email(self):
        self.assertEqual('rodrigao_frei28@hotmail.com',str(self.cliente.email))


    def test_str_cliente_retornar_telefone(self):
        self.assertEqual('35 9.9070-8090',str(self.cliente.telefone))

    def test_str_cliente_retornar_cep(self):
        self.assertEqual('37540-000',str(self.cliente.cep))


