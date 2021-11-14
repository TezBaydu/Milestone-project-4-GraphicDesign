import uuid

from django.db import models
from django.conf import settings

class Package(models.Model):

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    list_1 = models.TextField()
    list_2 = models.TextField()
    list_3 = models.TextField()
    list_4 = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    company_name = models.TextField()
    slogan = models.TextField()
    what_company_does = models.TextField()
    colours = models.TextField()
    look_feel = models.TextField()

    def _generate_order_number(self):
        """
        Generate random unique order number UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method to set order number if not set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    company_name = models.CharField(Order, max_length=264, null=False, blank=False, editable=False)
    slogan = models.CharField(Order, max_length=264, null=False, blank=False, editable=False)
    what_company_does = models.CharField(Order, max_length=600, null=False, blank=False, editable=False)
    colours = models.CharField(Order, max_length=264, null=False, blank=False, editable=False)
    look_feel = models.CharField(Order, max_length=264, null=False, blank=False, editable=False)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override original save method to set line item if not set already and update order total
        """
        self.lineitem_total = self.order.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.order.sku} on order {self.order.order_number}'
