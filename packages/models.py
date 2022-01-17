from django.db import models


class Package(models.Model):

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    logo_count_request = models.DecimalField(max_digits=2, decimal_places=0)
    quality_request = models.CharField(max_length=254, null=True, blank=True)
    support_request = models.CharField(max_length=254, null=True, blank=True)
    production_days = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
