from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from accounts.forms.signup_form import SignupForm


class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )

        return HttpResponseRedirect("/accounts/login/")
