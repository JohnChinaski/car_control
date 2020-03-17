from rest_framework import serializers

from ..models import OwnerRegister, VehicleBrand, VehicleModel, Vehicle, VehicleType


class OwnerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerRegister
        fields = ['name', 'doc_number', 'user', 'registration']


class OwnerSerializer(serializers.ModelSerializer):
    vehicles = serializers.StringRelatedField(many=True)

    class Meta:
        model = OwnerRegister
        fields = ['name', 'doc_number', 'vehicles', 'registration']


class VehicleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
