from django.db import models


class Package(models.Model):

    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    logo_count_request = models.IntegerField()
    quality_request = models.TextField(null=True, blank=True)
    support_request = models.TextField(null=True, blank=True)
    production_days = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    company_name = models.CharField(
        max_length=100, null=True, blank=True, default='Company Name required')
    company_slogan = models.CharField(
        max_length=200, null=True, blank=True, default='Company Slogan required')
    company_description = models.CharField(
        max_length=500, null=True, blank=True, default='Company Description required')
    company_colors = models.CharField(
        max_length=100, null=True, blank=True, default='Company Colors required')
    company_look = models.CharField(
        max_length=100, null=True, blank=True, default='Company Look required')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
