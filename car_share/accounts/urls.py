from django.urls import path
from . import views

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("accounts", views.AccountsViews.as_view(), name="accounts"), 
    path("listings", views.ListingsViews.as_view(), name="listings")
]