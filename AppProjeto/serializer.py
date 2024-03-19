from rest_framework import serializers

from .models import UserModels

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModels
        fields = ['id_Gps', 'latitude', 'longitude']