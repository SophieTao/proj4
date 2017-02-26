from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
import urllib.request
import urllib.parse
import json


# ITEMS
def home(request):
	req = urllib.request.Request('http://models-api:8000/api/v1/meals/2')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse([resp],safe=False)

def meal(request, meal_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/meals/' + meal_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse([resp], safe=False)

def comment(request, comment_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/comments/' + comment_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse([resp], safe=False)
	
def profile(request, profile_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/profiles/' + profile_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse([resp], safe=False)
