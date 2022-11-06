from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ListingsModel

# Context: Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website
# Using class-based views allows us to use the DRY principle
# Create views are meant to perform the following actions: Create a new item 

# single point of control
listing_model = ListingsModel 
listing_fields = ['title', 'description', 'rented']
listing_success_url = reverse_lazy('listings')


class ListingsViewRead(DetailView):
    model = listing_model
    fields = listing_fields
    success_url = listing_success_url

class ListingsViewCreate(CreateView):
    model = listing_model
    fields = listing_fields
    success_url = listing_success_url

class ListingsViewDelete(DeleteView):
    model = listing_model
    fields = listing_fields
    success_url = listing_success_url

    
    
