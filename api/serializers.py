from rest_framework import serializers
from .models import Location, OwnerType, Owner, PropertyType, TransactionType, Property

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'department', 'city', 'district']

class OwnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerType
        fields = ['id', 'name']

class OwnerSerializer(serializers.ModelSerializer):
    owener_type = OwnerTypeSerializer(read_only=True)
    owener_type_id = serializers.PrimaryKeyRelatedField(
        queryset=OwnerType.objects.all(),
        source='owener_type',
        write_only=True
    )

    class Meta:
        model = Owner
        fields = ['id', 'name', 'owener_type', 'owener_type_id']

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name']

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id', 'name']

class PropertySerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    transaction_type = TransactionTypeSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    onwer = OwnerSerializer(read_only=True)
    
    property_type_id = serializers.PrimaryKeyRelatedField(
        queryset=PropertyType.objects.all(),
        source='property_type',
        write_only=True
    )
    transaction_type_id = serializers.PrimaryKeyRelatedField(
        queryset=TransactionType.objects.all(),
        source='transaction_type',
        write_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location',
        write_only=True
    )
    onwer_id = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(),
        source='onwer',
        write_only=True
    )

    class Meta:
        model = Property
        fields = [
            'id', 'property_type', 'property_type_id', 'transaction_type', 'transaction_type_id',
            'location', 'location_id', 'onwer', 'onwer_id', 'address', 'stratum', 'floor',
            'rooms', 'age', 'area', 'latitude', 'longitude', 'publication_date',
            'publication_year', 'publication_month', 'price_by_m2', 'total_price',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

# Serializer para uso en listados (más ligero)
class PropertyListSerializer(serializers.ModelSerializer):
    property_type_name = serializers.CharField(source='property_type.name', read_only=True)
    transaction_type_name = serializers.CharField(source='transaction_type.name', read_only=True)
    location_str = serializers.CharField(source='location.__str__', read_only=True)
    owner_name = serializers.CharField(source='onwer.name', read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'property_type_name', 'transaction_type_name', 'location_str', 
            'owner_name', 'address', 'area', 'total_price', 'publication_date'
        ]