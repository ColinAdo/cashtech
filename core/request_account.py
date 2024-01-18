from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Account

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
