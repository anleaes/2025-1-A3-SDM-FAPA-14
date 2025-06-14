from .models import Review
from rest_framework import viewsets
from .serializer import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', 'client', 'hosting']