from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, editable=True, max_length=14)
    nome = models.CharField(max_length=45)
    cep = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)
    telefone = models.CharField(max_length=14, blank=True, null=True)

