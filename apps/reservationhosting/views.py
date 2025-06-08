from .models import ReservationHosting
from rest_framework import viewsets
from .serializer import ReservationHostingSerializer

# Create your views here.
class ReservationHostingViewSet(viewsets.ModelViewSet):
    queryset = ReservationHosting.objects.all()
    serializer_class = ReservationHostingSerializer