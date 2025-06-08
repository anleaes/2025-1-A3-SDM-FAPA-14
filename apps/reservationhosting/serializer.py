from .models import ReservationHosting
from rest_framework import serializers

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationHosting
        fields = '__all__'