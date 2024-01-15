from django.shortcuts import render
from django.db.models import Q

from account.models import Account  

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