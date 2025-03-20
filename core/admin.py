from django.contrib import admin
from.models import OwnerType, Owner, PropertyType, TransactionType, Location, Property

# Register your models here.
admin.site.register(OwnerType)
admin.site.register(Owner)
admin.site.register(PropertyType)
admin.site.register(TransactionType)
admin.site.register(Location)
admin.site.register(Property)