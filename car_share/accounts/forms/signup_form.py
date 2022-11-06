import datetime

from django import forms
from django.contrib.auth.models import User
from django.core import validators
from re import search
from datetime import date


class SignupForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    email = forms.CharField(max_length=120,
                            validators=[validators.EmailValidator(message="Enter a valid email address")],
                            required=False)
    first_name = forms.CharField(max_length=120, required=False)
    last_name = forms.CharField(max_length=120, required=False)
    date = forms.DateField()

    def clean(self):
        data = super().clean()
        cleaned_data = {}
        contains_username = False
        contains_password1 = False
        contains_dob = False
        contains_email = False
        contains_first_name = False
        contains_last_name = False

        for key, value in data.items():
            if key == 'username':
                contains_username = True
                cleaned_data['username'] = data['username']
            if key == 'password':
                contains_password1 = True
                cleaned_data['password'] = data['password']
            if key == 'email':
                contains_email = True
                cleaned_data['email'] = data['email']
            if key == 'first_name':
                contains_first_name = True
                cleaned_data['first_name'] = data['first_name']
            if key == 'last_name':
                contains_last_name = True
                cleaned_data['last_name'] = data['last_name']
            if key == 'date':
                contains_dob = True
                cleaned_data['date'] = data['date']

        if not contains_username:
            cleaned_data['username'] = ''
        if not contains_password1:
            cleaned_data['password'] = ''
        if not contains_email:
            cleaned_data['email'] = ''
        if not contains_first_name:
            cleaned_data['first_name'] = ''
        if not contains_last_name:
            cleaned_data['last_name'] = ''
        if not contains_dob:
            cleaned_data['date'] = ''

        if cleaned_data.get('username'):
            if User.objects.filter(username=cleaned_data.get('username')).exists():
                self.add_error('username', 'A user with that username already exists')
        if cleaned_data.get('password'):
            if len(cleaned_data.get('password')) < 8:
                self.add_error('password', 'This password is too short. It must contain at least 8 characters')
        if cleaned_data.get('email'):
            if not search(r"^[A-Za-z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", cleaned_data.get('email')):
                self.add_error('email', 'Enter a valid email address')
        if cleaned_data['username'] == '':
            self.add_error('username', 'This field is required')
        if cleaned_data['password'] == '':
            self.add_error('password', 'This field is required')

        return cleaned_data
    