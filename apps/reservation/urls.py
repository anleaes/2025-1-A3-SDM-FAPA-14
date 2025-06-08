from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reservation'

router = routers.DefaultRouter()
router.register('', views.ReservationViewSet, basename='reservas')

urlpatterns = [
    path('', include(router.urls))
]