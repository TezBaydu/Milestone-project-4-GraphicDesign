from django.contrib import admin
from .models import Package, Order


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'friendly_name',
        'list_1',
        'list_2',
        'list_3',
        'list_4',
        'image',
        'price',
    )

    ordering = ('sku',)


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date', 'price_total')

    fields = ('order_number', 'date', 'company_name',
              'slogan', 'what_company_does', 'colours',
              'look_feel', 'price_total',
              'full_name', 'email', 'phone_number',
              'town_or_city', 'street_address1',
              'street_address2', 'county', 'country',)

    list_display = ('company_name', 'slogan', 'what_company_does',
                    'colours', 'look_feel', 'price_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
admin.site.register(Package, PackageAdmin)
