from django.contrib import admin
from .models import Transaction, CreditCard


class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type']
    list_display = ['user', 'amount', 'status','transaction_type', 'reciever', 'sender']


class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'card_status', 'credit_type']
    list_display = ['user', 'amount', 'name', 'cvv', 'card_status', 'credit_type']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
