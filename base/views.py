import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreateRecordForm, RegisterForm
from .models import Record

logger = logging.getLogger(__name__)

'''
CBVs: 
-> record list
-> record creation
-> record update
-> record detail
-> delete record
'''


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
    else:
        records = Record.objects.all()
        context = {'records': records}
    return render(request, 'base/home.html', context)


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

# ==========================================================

class CreateRecordView(LoginRequiredMixin, CreateView):
    model = Record
    form_class =  CreateRecordForm
    template_name = "base/add_record.html"
    success_url = reverse_lazy('home')


class UpdateRecordView(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = CreateRecordForm
    template_name = 'base/update_record.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'record_id'


class DetailRecordView(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'base/record.html'
    context_object_name = 'customer_record'


class DeleteRecordView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy('home')
