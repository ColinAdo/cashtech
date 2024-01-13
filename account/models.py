from django.db import models
from shortuuid.django_fields import ShortUUIDField

import uuid

from userauths.models import User

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s_%s' % (instance.id, ext)

    return 'user_{0}/{1}'.format(instance.user.id, filename)

ACCOUNT_STATUS = (
    ('active', 'Active'),
    ('in-active', 'In-active'),
)

MARITAL_STATUS = (
    ('married', 'Married'),
    ('single', 'Single'),
    ('divorced', 'Divorced')
)

IDENTIFICATION_TYPE = (
    ('national_id', 'National ID'),
    ('driver_license', 'Driver License'),
    ('passport', 'Passport'),
)


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = ShortUUIDField(length=4, max_length=25, unique=True, prefix="ADO", alphabet='1234567890')
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(length=10, max_length=20, unique=True, prefix='217', alphabet='1234567890')
    pin_number = ShortUUIDField(length=4, max_length=7, unique=True, alphabet='1234567890')
    red_code = ShortUUIDField(length=10, max_length=20, unique=True, alphabet='1234567890')
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default='in-active')
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.user.username} account'
    

class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='KYC/profile', default='default.png')
    gender = models.CharField(max_length=20, choices=GENDER)
    identity_type = models.CharField(max_length=30, choices=IDENTIFICATION_TYPE)
    identity_image = models.ImageField(upload_to="KYC/identification", null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    signature = models.ImageField(upload_to='KYC/signiture')
    dob = models.DateTimeField(auto_now_add=False)

    # country
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    # contact
    mobile = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str_(self):
        return f'{self.full_name} KYC'
