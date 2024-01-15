from django.shortcuts import render, redirect
from django.contrib import messages

from .models import KYC, Account
from .forms import KYCForm

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
            new_kyc = form.save()
            new_kyc.user = user
            new_kyc.save()

            messages.success(request, "Kyc saved successfully")
            return redirect('index')
    else:
        form = KYCForm(instance=kyc)

    context = {
        'form': form,
        'kyc': kyc
    }
    return render(request,template, context)



