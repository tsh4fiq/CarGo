from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AccountModel

# Context: Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website
# Using class-based views allows us to use the DRY principle
# Create views are meant to perform the following actions: Create a new item 

account_model = AccountModel
account_fields = fields = ['title', 'description', 'complete']
account_success_url = reverse_lazy('accounts')

class AccountsViewsCreate(CreateView):
    model = account_model 
    fields = account_fields
    success_url = account_success_url

class AccountsViewsUpdate(UpdateView):
    model = account_model 
    fields = account_fields
    success_url = account_success_url

class AccountsViewsRead(DetailView):
    model = account_model
    fields = account_fields
    success_url = account_success_url

class AccountsViewsDelete(DeleteView):
    model = account_model 
    fields = account_fields
    success_url = account_success_url