from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ReviewModel

# Context: Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website
# Using class-based views allows us to use the DRY principle
# Create views are meant to perform the following actions: Create a new item 

reviews_model = ReviewModel
reviews_fields = ['title', 'description']

class ReviewsViews(CreateView):
    model = reviews_model
    fields = reviews_fields