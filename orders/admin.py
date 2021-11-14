from django.contrib import admin
from .models import Package


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

admin.site.register(Package, PackageAdmin)
