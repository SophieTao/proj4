from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

models_endpoint = 'http://models-api:8002/'

# ITEMS
def meals(request):
	json = request_get('api/v1/meals')
	return JsonResponse(json)

def request_get(endpoint):
	req = urllib.request.Request(models_endpoint + endpoint)
	raw = urllib.request.urlopen(req).read().decode('utf-8')
	return json.loads(raw)
