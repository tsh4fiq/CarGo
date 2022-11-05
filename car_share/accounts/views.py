from django.shortcuts import render
from django.http import HttpResponse

# Views is a webpage (basically) and this code serves HTTP requests and lets stuff show up on our website

def login(response):
    return HttpResponse("login.html")

def account_profile(response):
    return HttpResponse("account_profile.html")

def sign_up(response):
    return HttpResponse("sign_up.html")