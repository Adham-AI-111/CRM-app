from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, CreateRecordForm
from .models import Record
import logging

logger = logging.getLogger(__name__)

# ==============================================================
# @login_required
# def display_record(request, pk):
#   customer_record = Record.objects.get(id=pk)
#   return render(request, 'base/record.html', {'customer_record': customer_record})


# @login_required
# def delete_record(request, pk):
#     customer_record = Record.objects.get(id=pk)
#     customer_record.delete()
#     messages.success(request, "Record deleted successfully.")
#     logger.info('record was deleted', extra={'record_id': pk})
    
#     return redirect('home')


# @login_required
# def update_record(request, pk):
#     record = Record.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CreateRecordForm(request.POST, instance=record)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Record updated successfully.")
#             return redirect('home')
#         else:
#             form = CreateRecordForm(instance=record)
#     return render(request, 'base/update_record.html', {'form':form})


# @login_required
# def add_record(request):
#     if request.method == 'POST':
#         form = CreateRecordForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 messages.success(request, "Record added successfully.")
#                 logger.info("Record added successfully.", extra={'user_id': request.user.id})
#                 return redirect("home")

#             except Exception:
#                 logger.exception(f"Failed to create a record")

#     else:
#         form = CreateRecordForm()

#     return render(request, "base/add_record.html", {"form": form})