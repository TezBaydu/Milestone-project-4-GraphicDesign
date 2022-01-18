from django.contrib import admin
from .models import UserEnquiry


class UserEnquiryAdmin(admin.ModelAdmin):
    readonly_fields = ('enquiry_number', 'enquiry_date',
                       'full_name', 'email',
                       'message',)

    list_display = ('enquiry_number', 'enquiry_date', 'full_name',)

    ordering = ('-enquiry_date',)


admin.site.register(UserEnquiry, UserEnquiryAdmin)
