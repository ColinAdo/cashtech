from django import forms
from django.forms import ImageField, FileInput, DateInput

from.models import KYC

class DateInput(forms.DateInput):
    input_type = 'date' # Allow user to select date and time

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    signature = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = [
            'full_name',
            'image',
            'gender',
            'identity_type',
            'identity_image',
            'marital_status',
            'signature',
            'dob',
            'country',
            'state',
            'city',
            'mobile',
            'fax',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'Full Name'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'state': forms.TextInput(attrs={'placeholder':'State'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'mobile': forms.TextInput(attrs={'placeholder':'Mobile'}),
            'fax': forms.TextInput(attrs={'placeholder':'Fax'}),
            'dob': DateInput,
        }

