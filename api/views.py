from django.shortcuts import render
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Location, OwnerType, Owner, PropertyType, TransactionType, Property
from .serializers import LocationSerializer, OwnerTypeSerializer, OwnerSerializer, PropertyTypeSerializer, TransactionTypeSerializer, PropertySerializer, PropertyListSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar ubicaciones.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class OwnerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar tipos de propietarios.
    """
    queryset = OwnerType.objects.all()
    serializer_class = OwnerTypeSerializer
    permission_classes = [IsAuthenticated]


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar propietarios.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]


class PropertyTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar tipos de propiedades.
    """
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticated]


class TransactionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar tipos de transacciones.
    """
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    permission_classes = [IsAuthenticated]


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar propiedades inmobiliarias.
    Proporciona funcionalidades CRUD completas.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        """
        Usa un serializer diferente para las acciones de listado
        para optimizar el rendimiento y reducir la carga de datos.
        """
        if self.action == 'list':
            return PropertyListSerializer
        return PropertySerializer
    
   
