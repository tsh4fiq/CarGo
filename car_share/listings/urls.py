from django.urls import path
from . import views

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("listings", views.ListingsView.as_view(), name="listings"), 
    ]