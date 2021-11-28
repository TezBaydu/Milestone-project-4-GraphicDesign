from django.contrib import admin
from .models import Package, CompanyDetails


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



class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'company_name', 
        'company_slogan',
        'company_description',
        'company_colors',
        'company_look', 
    )

    ordering = ('sku',)


admin.site.register(CompanyDetails, CompanyDetailsAdmin)
