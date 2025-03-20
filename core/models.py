from django.db import models

class Location(models.Model):
    department = models.Charfield(max_Length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    
    
    class Meta:
        unique_together = ('department', 'city', 'district')
        
    def __str__(self):
        return f'{self.department},{self.city},{self.district}'
