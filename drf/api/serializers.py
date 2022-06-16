from rest_framework import serializers
from .models import Brand, Vehicle

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

# class BrandSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     country = serializers.CharField()
#
#     def create(self, validated_data):
#         return Brand.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.country = validated_data.get('country')
#         instance.save()
#         return instance
