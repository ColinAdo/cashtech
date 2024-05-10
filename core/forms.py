from django import forms

from .models import CreditCard

# Credit Card form 
class CreditCardForm(forms.ModelForm):
    
    class Meta:
        model = CreditCard
        fields = [
            'name',
            'amount',
            'number',
            'month',
            'year',
            'cvv',
            'credit_type',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Card Name'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Amount'}),
            'number': forms.TextInput(attrs={'placeholder': 'Card Number'}),
            'month': forms.TextInput(attrs={'placeholder': 'Expiry Month'}),
            'year': forms.TextInput(attrs={'placeholder': 'Expiry Year'}),
            'cvv': forms.TextInput(attrs={'placeholder': 'Card Cvv'}),
        }
