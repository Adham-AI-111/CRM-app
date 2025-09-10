from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    return render(request, 'base/home.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
            return render(request, 'base/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'base/register.html', {'form': form})
    return render(request, 'base/register.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')