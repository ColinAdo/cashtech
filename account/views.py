from django.shortcuts import render, redirect
from django.contrib import messages

from .models import KYC, Account
from .forms import KYCForm

from core.forms import CreditCardForm
from core.models import CreditCard

from decimal import Decimal


def account(request):
    template = 'account/account.html'
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You have not submitted your KYC')
        return redirect('kyc')
    
    account = Account.objects.get(user=request.user)
    context = {
        'kyc': kyc,
        'account': account,
    }
    return render(request, template, context)

def kyc_registration(request):
    template = 'account/kyc_reg_form.html'
    user = request.user
    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_kyc = form.save(commit=False)
            new_kyc.user = user
            new_kyc.save()

            messages.success(request, "Kyc saved successfully")
            return redirect('account')
    else:
        form = KYCForm(instance=kyc)

    context = {
        'form': form,
        'kyc': kyc
    }
    return render(request,template, context)


def dashboard(request):
    template = 'account/dashboard.html'
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You have not submitted your KYC')
        return redirect('kyc')

    account = Account.objects.get(user=request.user)
    credit_card = CreditCard.objects.filter(user=request.user)

    form = CreditCardForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.user = request.user
            new_card.save()

            messages.success(request, 'Added card successfully')
            return redirect('dashboard')
    else:
        form = CreditCardForm()

    context = {
        'kyc': kyc,
        'account': account,
        'form': form,
        'credit_card': credit_card
    }
    return render(request, template, context)

def delete_card(request, credit_id):
    credit_card = CreditCard.objects.get(credit_id=credit_id)
    account = request.user.account

    if credit_card.amount > 0:
        account.account_balance += credit_card.amount
        account.save()

        credit_card.delete()
        messages.success(request, 'Card deleted successfully')
        return redirect('dashboard')
    
    credit_card.delete()
    messages.success(request, 'Card deleted successfully')
    return redirect('dashboard')


def card_detail(request, credit_id):
    template = 'account/card_detail.html'
    account = Account.objects.get(user=request.user)
    credit_card = CreditCard.objects.get(credit_id=credit_id, user=request.user)

    context = {
        'account': account,
        'credit_card': credit_card
    }

    return render(request, template, context)

def fund_credit_card(request, credit_id):
    credit_card = CreditCard.objects.get(credit_id=credit_id)
    account = request.user.account
    

    if request.method == 'POST':
        amount = Decimal(request.POST.get('funding_amount'))

        if Decimal(amount) < float(account.account_balance):
            print(amount)
            print(type(amount))

            account.account_balance -= amount
            account.save()

            credit_card.amount += amount
            credit_card.save()

            messages.success(request, 'Credit card is Funded Successfully')
            return redirect('card_detail', credit_id)
        else:
            messages.warning(request, 'You have insufficient funds')
            return redirect('card_detail', credit_id)
        
    else:
        return redirect('card_detail', credit_id)


        

