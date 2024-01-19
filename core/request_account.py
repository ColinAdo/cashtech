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
            status='request_processing',
            transaction_type='request'
        )

        new_transaction.save()

        transaction_id = new_transaction.transaction_id

        return redirect('request_confirm', account_number, transaction_id)
    else:
        messages.warning(request, 'Try again later!')
        return redirect('account')
    
def request_confirm(request, account_number, transaction_id):
    template = 'request-account/request_confirm.html'

    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, template, context)

def request_processing(request, account_number, transaction_id):
    template = 'request-account/request_processing.html'
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    if request.method == 'POST':
        pin = request.POST.get('pin-number')

        if pin == request.user.account.pin_number:
            transaction.status = 'request_sent'
            transaction.save()

            transaction_id=transaction.transaction_id

            messages.success(request, 'Payment Request Sent Successfully!')
            return redirect('request_complete', account_number, transaction_id)
        else:
            messages.warning(request, 'Wrong Pin!')
            return redirect('request_confirm', account_number, transaction_id)

    else:
        messages.warning(request, 'Try Again Later!')
        return redirect('dashboard')
    
def request_complete(request, account_number, transaction_id):
    template = 'request-account/request_complete.html'
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, template, context)


def confirm_settlement(request, account_number, transaction_id):
    template = 'request-account/confirm_settlement.html'
    
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, template, context)

def process_settlement(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    sender_account = request.user.account

    if request.method == 'POST':
        pin = request.POST.get('pin-number')

        if pin == sender_account.pin_number:
            if float(sender_account.account_balance) > (transaction.amount):
                sender_account.account_balance -= transaction.amount
                sender_account.save()

                account.account_balance += transaction.amount
                account.save()

                transaction.status = 'request_settled'
                transaction.save()

                messages.success(request, f'{transaction.amount} was settled to {account.user.username}')
                return redirect('complete_settlement', account_number, transaction_id)
            else:
                messages.warning(request, 'You have insufficient balance!')
            
        else:
            messages.warning(request, 'Wrong Pin!')
            return redirect('confirm_settlement', account_number, transaction_id)

    else:
        messages.warning(request, 'Try again later!')
        return redirect('dashboard')
    

def complete_settlement(request, account_number, transaction_id):
    template = 'request-account/request_complete.html'
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, template, context)
