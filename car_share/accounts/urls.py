from django.urls import path
from .views import AccountsViewsCreate, AccountsViewsDelete, AccountsViewsRead, AccountsViewsUpdate

# URL files defined the path to our different web-pages (aka endpoints)

url_patterns = [
    path("accounts-create", AccountsViewsCreate.as_view(), name="accounts"), 
    path("accounts-delete", AccountsViewsDelete.as_view(), name="accounts"), 
    path("accounts-read", AccountsViewsRead.as_view(), name="accounts"), 
    path("accounts-update", AccountsViewsUpdate.as_view(), name="accounts"), 
    ]