from django.shortcuts import render, redirect
from django.core import serializers
from .forms import CreateAccountForm, CreateListingForm, LoginForm
import urllib
import urllib.request
import urllib.parse
import json

def home(request):
    req = urllib.request.Request('http://exp-api:8000/home/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)  
    context = {'meals': resp[0],'allcomments': resp[1]}
    return render(request, 'api/index.html', context)

def meal(request, cafe_id):
		req1 = urllib.request.Request('http://exp-api:8000/meal/'+ cafe_id)
		resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
		resp = json.loads(resp_json1)
		context = {'resp': resp}
		return render(request, 'api/meal.html', context)

def comment(request, comment_id):
		req1 = urllib.request.Request('http://exp-api:8000/comment/'+ comment_id)
		resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
		resp1 = json.loads(resp_json1)
		context1 = {'resp': resp1}
		return render(request, 'api/comment.html', context1)

def login(request):
	if request.method == 'GET':
		next = request.GET.get('next') or reverse('index')
		form = LoginForm()
		return render(request, 'api/login.html', {'form': form, 'next': next})
	form = LoginForm(request.POST)
	if not form.is_valid():
		return render(request, 'api/login.html', {'form': form})
	email = form.cleaned_data['email']
	password = form.cleaned_data['password']
	next = form.cleaned_data.get('next') or reverse('index')
	post_data = {'email': email, 'password': password}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp-api:8000/login/', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	if not resp or not resp['ok']:
		return render(request, 'api/login.html', {'form': form, 'error': True})
	authenticator = resp['result']['authenticator']
	response = HttpResponseRedirect(next)
	response.set_cookie("auth", authenticator["authenticator"])
	return response


def create_account(request):
	if request.method == 'GET':
		form = CreateAccountForm()
		return render(request, 'api/create_account.html', {'form': form})
	form = CreateAccountForm(request.POST)
	if not form.is_valid():
		return render(request, 'api/create_account.html', {'form': form})
	username = form.cleaned_data['username']
	email = form.cleaned_data['email']
	password = form.cleaned_data['password']
	post_data = {'username': username,
				 'email': email,
				 'password': password,}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp-api:8000/create_account/', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	if not resp or not resp['ok']:
		return render(request, 'api/create_account.html', {'form': form, 'error': True})
	post_data = {'email': email, 'password': password}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp-api:8000/login/', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	authenticator = resp['result']['authenticator']
	response = HttpResponseRedirect(reverse('index'))
	response.set_cookie("auth", authenticator["authenticator"])
	return response

