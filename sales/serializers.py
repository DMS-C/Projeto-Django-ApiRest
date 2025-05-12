from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.name')
    car_details = serializers.ReadOnlyField(source='car.model')

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'customer_name', 'car', 'car_details', 'sale_date', 'value', 'payment_method']
        
    def validate(self, data):
        if data['car'].status == 'sold':
            raise serializers.ValidationError(f"Carro {data['car'].model} já foi vendido.")
        return data
    
    def create(self, validated_data):
        car = validated_data['car']
        car.status = 'sold'
        car.save()
        return super().create(validated_data)