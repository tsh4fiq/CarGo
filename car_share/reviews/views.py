from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ReviewModel

# Context: Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website
# Using class-based views allows us to use the DRY principle
# Create views are meant to perform the following actions: Create a new item 

reviews_model = ReviewModel
reviews_fields = ['title', 'description']
reviews_success_url = reverse_lazy('reviews')

class ReviewsViewsCreate(CreateView):
    model = reviews_model
    fields = reviews_fields
    success_url = reviews_success_url

class ReviewsViewsRead(DetailView):
    model = reviews_model
    fields = reviews_fields
    success_url = reviews_success_url