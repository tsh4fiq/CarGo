from django.urls import path
from .views import ReviewsViewsCreate, ReviewsViewsRead

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("reviews/create", ReviewsViewsCreate.as_view(), name="reviews"), 
    path("reviews/read", ReviewsViewsRead.as_view(), name="reviews"), 
    ]