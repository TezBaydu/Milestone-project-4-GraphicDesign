from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserEnquiry
from profiles.models import UserProfile

import json
import time


class EnquiryWH_Handler:
    """Handle Enquiry webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, enquiries):
        """Send the user a confirmation email"""
        cust_email = enquiries.email
        subject = render_to_string(
            'enquiries/enquiry_emails/enquiry_email_subject.txt',
            {'enquiries': enquiries})
        body = render_to_string(
            'enquiries/enquiry_emails/enquiry_email_body.txt',
            {'enquiries': enquiries,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

        self._send_confirmation_email(enquiries)

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

        self._send_confirmation_email(enquiries)
