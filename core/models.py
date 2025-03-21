from django.db import models


OWNER_TYPES =(
        ('Inmobiliaria', 'Inmobiliaria'),
        ('Particular', 'Particular')
    )


PROPERTY_TYPES =(
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Local', 'Local'),
        ('Oficina', 'Oficina'),
        ('Bodega', 'Bodega')
)

TRANSACTION_TYPES =(
        ('Venta', 'Venta'),
        ('Arriendo', 'Arriendo')
)

AGE_TYPES=(
    ('1 a 8 años','1 a 8 años'),
    ('9 a 15 años','9 a 15 años'),
    ('16 a 30 años','16 a 30 años'),
    ('Más de 30 años','Más de 30 años'),
)


class OwnerType(models.Model):
    name = models.CharField(choices=OWNER_TYPES, max_length=100, unique=True )
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length =255)
    owener_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class PropertyType(models.Model):
    name = models.CharField(choices=PROPERTY_TYPES, max_length=100, unique=True )
    
    def __str__(self):
        return self.name

class TransactionType(models.Model):
    name = models.CharField(choices=TRANSACTION_TYPES, max_length=100, unique=True, )
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    department = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    
    
    class Meta:
        unique_together = ('department', 'city', 'district')
        
    def __str__(self):
        return f'{self.department},{self.city},{self.district}'
    
class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    onwer = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    stratum = models.CharField(max_length=255, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    age = models.CharField(choices=AGE_TYPES, max_length=50, null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    publication_date = models.DateField()
    publication_year = models.IntegerField()
    publication_month = models.CharField(max_length=20)
    price_by_m2 =models.DecimalField(max_digits=15, decimal_places=2)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    
    
    
    