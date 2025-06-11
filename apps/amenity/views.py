from .models import Amenity
from rest_framework import viewsets
from .serializer import AmenitySerializer

# Create your views here.
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer