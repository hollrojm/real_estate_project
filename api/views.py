from django.shortcuts import render
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from core.models import Location, OwnerType, Owner, PropertyType, TransactionType, Property , AGE_TYPES
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
    
    @action(detail=False, methods=['get'])
    def ages(self, request):
        """
        Returns all available property age types.
        """
        age_types = [age[0] for age in AGE_TYPES]
        return Response(age_types)
    
    
    
class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar ubicaciones.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def find_or_create(self, request):
        """
        Busca una ubicación existente por departamento, ciudad y distrito
        o crea una nueva si no existe.
        """
        department = request.data.get('department')
        city = request.data.get('city')
        district = request.data.get('district')
        
        if not all([department, city, district]):
            return Response(
                {"detail": "Departamento, ciudad y distrito son requeridos"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
       
        try:
            location = Location.objects.get(
                department=department,
                city=city,
                district=district
            )
            serializer = self.get_serializer(location)
            return Response(serializer.data)
        except Location.DoesNotExist:
            # Crear nueva ubicación si no existe
            new_location_data = {
                'department': department,
                'city': city,
                'district': district
            }
            serializer = self.get_serializer(data=new_location_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    @action(detail=False, methods=['get'])
    def by_department(self, request):
        """
        Retorna todas las locaciones filtradas por departamento.
        """
        department = request.query_params.get('department', None)
        if not department:
            return Response(
            {"detail": "Parámetro 'department' es requerido"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Filtrar locaciones por departamento
        locations = Location.objects.filter(department=department)
    
    # Agrupar por ciudad y distrito
        result = {}
        for location in locations:
            if location.city not in result:
                result[location.city] = []
        
            if location.district not in result[location.city]:
                result[location.city].append(location.district)
    
        return Response(result)
    
    
