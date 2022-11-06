from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AccountModel

# Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website
class AccountsViews(CreateView):
    model = AccountModel # we're using our own model here
    fields = ['title', 'description', 'complete']
    # success_url: reverse_lazy('tasks')