from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from account.models import Account  
from .models import Transaction

from decimal import Decimal

def search_account(request):
    template = 'transfer/search_account.html'

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

def transfer_ammount(request, account_number):
    template = 'transfer/transfer_amount.html'
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request, 'Account number does not exist!')
        return redirect('search')
    context = {
        'account': account
    }
    return render(request, template, context)

def transaction(request, account_number):
    user = request.user
    account = Account.objects.get(account_number=account_number)

    sender = user
    reciever = account.user

    reciever_account = account
    sender_account = user.account

    amount = request.POST.get('amount')
    description = request.POST.get('description')

    if request.method == 'POST':
        if float(sender_account.account_balance) >= float(amount):
            new_transaction = Transaction.objects.create(
                user=user,
                amount=amount,
                description=description,
                reciever=reciever,
                sender=sender,
                reciever_account=reciever_account,
                sender_account=sender_account,
                status='processing',
                transaction_type='transfer'
            )

            new_transaction.save()

            transaction_id = new_transaction.transaction_id

            return redirect('search_account') # redirect TO CONFIRM TRANSFER
        else:
            messages.warning(request, 'You do not have sufficient balance')
            return redirect('transfer_amount', account_number)
    else:
        return redirect('search_account')