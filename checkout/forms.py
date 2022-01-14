from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country', 'company_name', 'company_slogan',
                  'company_description', 'company_colors',
                  'company_look',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes and remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country',
            'company_name': 'Logo Name',
            'company_slogan': 'Slogan or Strapline',
            'company_description': 'Company Description',
            'company_colors': 'Preferred Colours',
            'company_look': 'Look and Feel',
        }

        # self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
