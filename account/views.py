from django.shortcuts import render, redirect
from django.contrib import messages

from .models import KYC
from .forms import KYCForm

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



