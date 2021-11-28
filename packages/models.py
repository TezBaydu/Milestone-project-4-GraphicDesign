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

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CompanyDetails(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    company_name = models.CharField(
        max_length=100, null=False, blank=False, default=0)
    company_slogan = models.CharField(
        max_length=200, null=False, blank=False, default=0)
    company_description = models.CharField(
        max_length=500, null=False, blank=False, default=0)
    company_colors = models.CharField(
        max_length=100, null=False, blank=False, default=0)
    company_look = models.CharField(
        max_length=100, null=False, blank=False, default=0)

    def __str__(self):
        return self.company_name
