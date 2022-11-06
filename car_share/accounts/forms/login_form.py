from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)

    def clean(self):
        data = super().clean()
        cleaned_data = {}
        contains_username = False
        contains_password = False

        for key, value in data.items():
            if key == 'username':
                contains_username = True
                cleaned_data['username'] = data['username']
            if key == 'password':
                contains_password = True
                cleaned_data['password'] = data['password']

        if cleaned_data['username'] == '':
            self.add_error('username', 'This field is required')
        if cleaned_data['password'] == '':
            self.add_error('password', 'This field is required')

        if not (user := authenticate(username=data.get('username'), password=data.get('password'))):
            self.add_error('password', 'Username or password is invalid')

        cleaned_data['user'] = user

        return cleaned_data
