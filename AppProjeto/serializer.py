from rest_framework import serializers

from .models import UserModels

def ValidaNumero(value):
    try:
        float(value)
    except ValueError:
        raise serializers.ValidationError("BAD_REQUEST_400")    


class UserSerializer(serializers.ModelSerializer):
    latitude = serializers.CharField(validators=[ValidaNumero])
    longitude = serializers.CharField(validators=[ValidaNumero])

    class Meta:
        model = UserModels
        fields = ['id_Gps', 'latitude', 'longitude']