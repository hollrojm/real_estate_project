from rest_framework import serializers
from core.models import Location, OwnerType, Owner, PropertyType, TransactionType, Property

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OwnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerType
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    owener_type = OwnerTypeSerializer(read_only=True)
    owener_type_id = serializers.PrimaryKeyRelatedField(
        queryset=OwnerType.objects.all(),
        source='owener_type',
        write_only=True
    )

    class Meta:
        model = Owner
        fields = '__all__'

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.name')
    

    class Meta:
        model = Property
        fields = '__all__'
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