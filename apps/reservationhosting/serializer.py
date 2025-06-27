from .models import ReservationHosting
from rest_framework import serializers

class ReservationHostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationHosting
        fields = '__all__'
        depth = 2