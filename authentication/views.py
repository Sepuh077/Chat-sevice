from django.shortcuts import redirect, render
from .models import Profile
from .forms import *
from django.contrib.auth import authenticate, login as sign_in, logout as sign_out


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    error_message = False
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(username=email, password=password)
            
            if user:
                sign_in(request, user)
                return redirect('home')
            else:
                error_message = True
    
    context = {
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'authentication/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {
        'form': form,
    }
    return render(request, 'authentication/register.html', context)


def authentication(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    login_form = LoginForm()
    register_form = RegisterForm()
    error_message = False
    
    if request.method == "POST":
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                
                user = authenticate(username=email, password=password)
                
                if user:
                    sign_in(request, user)
                    return redirect('home')
                else:
                    error_message = True
        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
        
            if register_form.is_valid():
                register_form.save()
                return redirect('login')
    
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'error_message': error_message,
    }
    return render(request, 'authentication/auth.html', context)


def logout(request):
    sign_out(request)
    return redirect('login')
