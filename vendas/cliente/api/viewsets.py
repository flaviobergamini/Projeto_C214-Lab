from rest_framework import viewsets
from cliente.api import serializers
from cliente import models

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()