from rest_framework import serializers
from .models import Farm, SensorData
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'