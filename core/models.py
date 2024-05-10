from django.db import models
from shortuuid.django_fields import ShortUUIDField

from userauths.models import User
from account.models import Account

# Transaction Choices 
TRANSACTION_TYPE = (
    ("transfer", "Transfer"),
    ("recieved", "Recieved"),
    ("withdraw", "withdraw"),
    ("refund", "Refund"),
    ("request", "Payment Request"),
    ("none", "None")
)

# Transaction Status choice 
TRANSACTION_STATUS = (
    ("failed", "failed"),
    ("completed", "completed"),
    ("pending", "pending"),
    ("processing", "processing"),
    ("request_sent", "request_sent"),
    ("request_settled", "request settled"),
    ("request_processing", "request processing"),
)

# Credit type choice 
CREDIT_TYPE = (
    ("visa", "visa"),
    ("master", "master"),
    ("vivo", "vivo"),
    
)

# Transaction model 
class Transaction(models.Model):
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1000, null=True, blank=True)

    reciever = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reciever")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")

    reciever_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="reciever_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="sender_account")

    status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="pending")
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="none")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        try:
            return f"{self.user}"
        except:
            return f"Transaction"

class CreditCard(models.Model):
    credit_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="CRD")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    credit_type = models.CharField(max_length=100, choices=CREDIT_TYPE)
    card_status = models.BooleanField(default=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} Card'
