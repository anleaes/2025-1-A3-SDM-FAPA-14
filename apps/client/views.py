from .models import Client
from rest_framework import viewsets
from .serializer import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'cell_phone']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]