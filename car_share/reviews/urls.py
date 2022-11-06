from django.urls import path
from . import views as 

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("reviews/create", views.ReviewsViewsCreate.as_view(), name="reviews"), 
    path("reviews/read", views.ReviewsViewsRead.as_view(), name="reviews"), 
    ]