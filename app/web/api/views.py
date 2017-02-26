from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
import urllib
import urllib.request
import urllib.parse
import json
from django.core.urlresolvers import reverse_lazy

def home(request):
    req = urllib.request.Request('http://exp-api:8000/home/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    context = {'profiles_list': resp,}
    return render(request, 'api/index.html', context)

def meal(request):
	req = urllib.request.Request('http://exp-api:8000/home/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	context = {'meals_list': resp,}
	return render(request, 'api/meal.html', context)