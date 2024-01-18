from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Account, Transaction

def request_account(request):
    template = 'request-account/request_account.html'

    account = Account.objects.all()

    query = request.POST.get('account_number')
    if query:
        account = account.filter(
            Q(account_number=query) | Q(user__email=query)
        ).distinct()

    context = {
        'account': account,
        'query': query
    }
    return render(request, template, context)


def request_ammount(request, account_number):
    template = 'request-account/request_amount.html'
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request, 'Account number does not exist!')
        return redirect('request_account')
    context = {
        'account': account
    }
    return render(request, template, context)

def request_transaction(request, account_number):
    template = 'request-account/request_transaction.html'
    account = Account.objects.get(account_number=account_number)

    user = request.user
    sender = user
    receiver = account.user

    sender_account = user.account
    receiver_account = account

    if request.method == 'POST':
        amount = request.POST.get('amount-request')
        description = request.POST.get('description')

        new_transaction = Transaction.objects.create(
            user=user,
            amount=amount,
            description=description,
            reciever=receiver,
            sender=sender,
            reciever_account=receiver_account,
            sender_account=sender_account,
            status='request_sent',
            transaction_type='request'
        )

        new_transaction.save()

        transaction_id = new_transaction.transaction_id

        messages.success(request, 'Payment Request Sent')
        return redirect('request_confirm', account_number, transaction_id)
    else:
        messages.warning(request, 'Try again later!')
        return redirect('account')