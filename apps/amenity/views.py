from .models import Amenity
from rest_framework import viewsets
from .serializer import AmenitySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']