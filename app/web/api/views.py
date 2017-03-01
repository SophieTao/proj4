from django.shortcuts import render, redirect
from django.core import serializers
import urllib
import urllib.request
import urllib.parse
import json

def home(request):
    req = urllib.request.Request('http://exp-api:8000/home/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)  
    context = {'recentmeals': resp[0],'allmeals': resp[1],'allcomments': resp[2]}
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




