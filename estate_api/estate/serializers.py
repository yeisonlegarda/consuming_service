from rest_framework import serializers
from estate.models import Property, Status, StatusHistory


class PropertySerializer(serializers.ModelSerializer):
    """Define serializer for estates"""
    class Meta:
        model = Property
        fields = ('address', 'city', 'description', 'price')


class StatusSerializer(serializers.ModelSerializer):
    """Define serializer for status"""

    class Meta:
        model = Status
        fields = ('id', 'name')


class StatusHistorySerializer(serializers.ModelSerializer):
    """Define serializer for status history related to estate"""
    property = PropertySerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = StatusHistory
        fields = ('property', 'status')
