from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm

def signup(request):
    template = 'userauths/sign-up.html'

    if request.user.is_authenticated:
        return redirect('index')  

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            messages.success(request, f'You have logged in successfully as {username}')

            new_user = authenticate(email=email, password=password)

            login(request, new_user)
            return redirect('index')
        
    else:
        form = SignupForm()


    context = {
        'form': form,
    }
    return render(request, template, context)
