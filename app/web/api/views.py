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
    context = {'recentmeals': resp[0],'allcomments': resp[1]}
    return render(request, 'api/index.html', context)

def meal(request, cafe_id):
		req1 = urllib.request.Request('http://exp-api:8000/meal/'+ cafe_id)
		resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
		resp1 = json.loads(resp_json1)
		context1 = {'meals_list': resp1}
		return render(request, 'api/meal.html', context1)

def comment(request, comment_id):
		req1 = urllib.request.Request('http://exp-api:8000/comment/'+ comment_id)
		resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
		resp1 = json.loads(resp_json1)
		context1 = {'comments_list': resp1}
		return render(request, 'api/comment.html', context1)




