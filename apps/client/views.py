from .models import Client
from rest_framework import viewsets
from .serializer import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'cell_phone']