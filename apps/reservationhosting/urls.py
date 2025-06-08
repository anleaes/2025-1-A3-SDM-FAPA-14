from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reservationhosting'

router = routers.DefaultRouter()
router.register('', views.ReservationHostingViewSet, basename='itens_reserva')

urlpatterns = [
    path('', include(router.urls)) 
]