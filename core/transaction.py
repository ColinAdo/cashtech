from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    template = 'transaction/transaction_list.html'
    sender_transaction = Transaction.objects.filter(sender=request.user)
    receiver_transaction = Transaction.objects.filter(reciever=request.user)

    context = {
        'sender_transaction': sender_transaction,
        'receiver_transaction': receiver_transaction
    }
    return render(request, template, context)


def transaction_detail(request, transaction_id):
    template = 'transaction/transaction_detail.html'
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'transaction': transaction,
    }
    return render(request, template, context)
