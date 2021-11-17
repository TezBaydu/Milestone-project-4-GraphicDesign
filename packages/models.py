from django.db import models


class Package(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    logo_count_request = models.IntegerField()
    quality_request = models.TextField(null=True, blank=True)
    support_request = models.TextField(null=True, blank=True)
    production_days = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


