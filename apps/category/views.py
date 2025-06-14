from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']