from django.urls import path
from . import views

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    
    path("", views.login, name="login"),
    path("", views.account_profile, name="account_profile"),
    path("", views.sign_up, name="sign_up")

]