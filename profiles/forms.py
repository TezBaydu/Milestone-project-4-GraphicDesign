from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes and remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',
            'default_company_name': 'Logo Name',
            'default_company_slogan': 'Slogan or Strapline',
            'default_company_description': 'Company Description',
            'default_company_colors': 'Preferred Colours',
            'default_company_look': 'Look & Feel e.g. Modern / Minimal / Fun',
        }

        # self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # if field != 'country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
