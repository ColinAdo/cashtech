from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_filter = ['account_status']
    list_display = ['user', 'account_status' ,'account_number', 'account_balance']


admin.site.register(Account, AccountAdmin)
