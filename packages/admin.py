from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'friendly_name',
        'price',
        'image',
        'logo_count_request',
        'quality_request',
        'support_request',
        'production_days',
    )

    ordering = ('sku',)

admin.site.register(Package, PackageAdmin)
