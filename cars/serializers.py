from rest_framework import serializers
from cars.models import Brand
from cars.models import Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__' 

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'