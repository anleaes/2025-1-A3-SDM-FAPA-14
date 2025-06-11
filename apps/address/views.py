from .models import Address
from rest_framework import viewsets
from .serializer import AddressSerializer

# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer