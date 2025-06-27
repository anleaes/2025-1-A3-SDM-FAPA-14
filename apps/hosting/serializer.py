from .models import Hosting
from rest_framework import serializers

class HostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosting
        fields = '__all__'
        depth = 1