from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description')
        model = City
