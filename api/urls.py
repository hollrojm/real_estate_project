from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, OwnerViewSet, LocationViewSet, OwnerTypeViewSet, PropertyTypeViewSet, TransactionTypeViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'owner_types', OwnerTypeViewSet)
router.register(r'property_types', PropertyTypeViewSet)
router.register(r'transaction_types', TransactionTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]