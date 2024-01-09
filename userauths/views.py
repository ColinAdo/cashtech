from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm
from .models import User

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

def signin(request):
    template = 'userauths/sign-in.html'

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,'you have logged in successfully')
                return redirect('index')
            else:
                messages.warning(request, 'Incorrect email or password')
        except:
            messages.warning(request, 'User does not exist')

    return render(request, template)

def signout(request):
    logout(request)
    messages.info(request, 'Logged out!')
    return redirect('signin')