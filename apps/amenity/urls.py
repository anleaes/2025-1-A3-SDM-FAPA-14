from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'amenity'

router = routers.DefaultRouter()
router.register('', views.AmenityViewSet, basename='Comodidades')

urlpatterns = [
    path('', include(router.urls))
]