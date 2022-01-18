import uuid

from django.db import models
from django.conf import settings


class UserEnquiry(models.Model):

    enquiry_number = models.CharField(
        max_length=32, null=False, editable=False)
    enquiry_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.CharField(
        max_length=500, null=False, blank=False)

    def _generate_enquiry_number(self):
        """
        Generate a random, unique enquiry number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the enquiry number
        if it hasn't been set already.
        """
        if not self.enquiry_number:
            self.enquiry_number = self._generate_enquiry_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.enquiry_number
