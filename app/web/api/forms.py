from django import forms
from django.contrib.admin import widgets

class LoginForm(forms.Form):
	name = forms.CharField(label='Name',max_length=32)
	email = forms.EmailField(label='Email')
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class CreateListingForm(forms.Form):
	name = forms.CharField(label='Name',max_length=32)
	location = forms.CharField(label='Location', max_length=32)
	description = forms.CharField(label='Description', max_length=300)	
	date = forms.CharField(label='Time',max_length=300)
	feedback = forms.CharField(label='Feedback', max_length=300)

class CreateAccountForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
