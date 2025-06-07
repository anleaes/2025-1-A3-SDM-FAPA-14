from .models import Hosting
from rest_framework import viewsets
from .serializer import HostingSerializer

# Create your views here.
class HostingViewSet(viewsets.ModelViewSet):
    queryset = Hosting.objects.all()
    serializer_class = HostingSerializer