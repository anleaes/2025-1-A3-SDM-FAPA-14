from .models import Review
from rest_framework import viewsets
from .serializer import ReviewSerializer

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer