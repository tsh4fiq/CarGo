from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from accounts.forms.login_form import LoginForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return HttpResponseRedirect('/accounts/dashboard/')
