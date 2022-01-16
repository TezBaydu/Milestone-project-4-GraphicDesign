from django import forms
from .models import Packages


class ProductForm(forms.ModelForm):

    class Meta:
        model = Packages
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
