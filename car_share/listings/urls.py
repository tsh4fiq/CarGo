from django.urls import path
from .views import ListingsViewRead, ListingsViewDelete, ListingsViewCreate

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("listings/create", ListingsViewCreate.as_view(), name="listings"), 
    path("listings/read", ListingsViewRead.as_view(), name="listings"), 
    path("listings/delete", ListingsViewDelete.as_view(), name="listings"), 
    ]