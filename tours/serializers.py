from rest_framework import serializers
from .models import Tour, DailyCity
from .models import City

class DailyCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCity
        fields = ('day_number', 'city', 'description')

class TourSerializer(serializers.ModelSerializer):
    days = DailyCitySerializer(many=True)  # Günlük şehirleri ekle

    class Meta:
        model = Tour
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'