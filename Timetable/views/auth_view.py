from ..models import User
from django.shortcuts import render, redirect
from ..forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user_model

def user_logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, 'You have been logged out.')
    else:
        messages.warning(request, 'You are not logged in.')

    return redirect('index')  


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print (email)
            print (password)

            
            try:
                user = get_user_model().objects.get(email=email)
                user = get_user_model().objects.get(password=password)
            except get_user_model().DoesNotExist:
                user = None


        if user is not None: 
            auth_login(request, user)
            messages.success(request, f'Welcome, {email}!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'auth.html', {'form': form})


