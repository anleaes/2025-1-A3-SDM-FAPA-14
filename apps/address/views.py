from .models import Address
from rest_framework import viewsets
from .serializer import AddressSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['street', 'number', 'postal_code']