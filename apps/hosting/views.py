from .models import Hosting
from rest_framework import viewsets
from .serializer import HostingSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class HostingViewSet(viewsets.ModelViewSet):
    queryset = Hosting.objects.all()
    serializer_class = HostingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'category']