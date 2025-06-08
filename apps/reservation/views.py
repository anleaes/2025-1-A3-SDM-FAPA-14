from .models import Reservation
from rest_framework import viewsets
from .serializer import ReservationSerializer

# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer