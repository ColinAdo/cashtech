from django.contrib import admin

from .models import Account, KYC

class AccountAdmin(admin.ModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_filter = ['account_status']
    list_display = ['user', 'account_status' ,'account_number', 'account_balance']

class KYCAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'country', 'dob']
    search_fields = ['full_name']


admin.site.register(Account, AccountAdmin)
admin.site.register(KYC, KYCAdmin)
