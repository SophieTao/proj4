from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
import urllib.request
import urllib.parse
import json

def home(request):
	#req = urllib.request.Request('http://models-api:8000/api/v1/meals/2')
	req = urllib.request.Request('http://models-api:8000/api/v1/allcomments')	
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)

	req1 = urllib.request.Request('http://models-api:8000/api/v1/recentmeals')
	resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
	resp1 = json.loads(resp_json1)
	return JsonResponse([resp1, resp],safe=False)

def meal(request, cafe_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/meals/' + cafe_id)
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
