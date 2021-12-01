import uuid

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

    class Meta:
        verbose_name_plural = 'Company Details'

    logo_request_number = models.CharField(max_length=32, null=False, editable=False)
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

    def _logo_request_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.logo_request_number

    def _company_name(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.logo_request_number:
            self.logo_request_number = self._logo_request_number()
        super().save(*args, **kwargs)
