from django import forms
from django.contrib.admin import widgets

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    next = forms.CharField(max_length=100)

class CreateListingForm(forms.Form):
	description = forms.CharField(max_length=1300)
	feedback = forms.CharField(max_length=300)

class CreateAccountForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
