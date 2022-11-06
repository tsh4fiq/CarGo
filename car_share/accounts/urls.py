from django.urls import path
from accounts.views.login import LoginView
from accounts.views.signup import SignupView
from accounts.views.dashboard import DashboardView
from django.conf.urls.static import static
from django.conf import settings

# URL files defined the path to our different web-pages (aka endpoints)
app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("signup/", SignupView.as_view(), name="sign_up")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
