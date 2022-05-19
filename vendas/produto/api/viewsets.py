from rest_framework import viewsets
from produto.api import serializers
from produto import models

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutoSerializer
    queryset = models.Produto.objects.all()