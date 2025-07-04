from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'cell_phone', 'gender', 'photo', 'doc']
        depth = 1