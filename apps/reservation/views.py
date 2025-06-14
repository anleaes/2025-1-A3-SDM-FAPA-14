from .models import Reservation
from rest_framework import viewsets
from .serializer import ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'checkin_date', 'checkout_date']