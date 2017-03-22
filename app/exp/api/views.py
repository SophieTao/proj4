from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
import urllib.request
import urllib.parse
import json
from django.core.exceptions import ObjectDoesNotExist


def home(request):
	#req = urllib.request.Request('http://models-api:8000/api/v1/meals/2')
	req = urllib.request.Request('http://models-api:8000/api/v1/allcomments')	
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)

	req1 = urllib.request.Request('http://models-api:8000/api/v1/recentmeals')
	resp_json1 = urllib.request.urlopen(req1).read().decode('utf-8')
	resp1 = json.loads(resp_json1)

	req2 = urllib.request.Request('http://models-api:8000/api/v1/allmeals')
	resp_json2 = urllib.request.urlopen(req2).read().decode('utf-8')
	resp2 = json.loads(resp_json2)

	if len(resp1) < 3:
		return JsonResponse([resp2, resp],safe=False)
	else:
		return JsonResponse([resp1, resp],safe=False)

def meal(request, cafe_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/meals/' + cafe_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp, safe=False)

def comment(request, comment_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/comments/' + comment_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp, safe=False)
	
def profile(request, profile_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/profiles/' + profile_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse([resp], safe=False)

############## user management (login, logout, create account) ###############


def logout(request):
	if request.method == "POST":
		post_encoded = urllib.parse.urlencode((request.POST).dict()).encode('utf-8')
		try:
			req = urllib.request.Request('http://models-api:8000/api/v1/auth/get/' + request.POST["pk"])
		except ObjectDoesNotExist:
			return JsonResponse("User not found", safe=False)	
		resp_json = urllib.request.urlopen(req).read().decode('utf-8') 
		resp = json.loads(resp_json)
		for i in resp:
			try:
				r = urllib.request.Request('http://models-api:8000/api/v1/auth/delete/' + str(i["authenticator"]))
			except ObjectDoesNotExist:
				return JsonResponse("Cannot delete authenticator", safe=False)	
			resp_json2 = urllib.request.urlopen(r).read().decode('utf-8')
		return JsonResponse("Successfully logout", safe=False)
	else:
		return JsonResponse("Must Post", safe=False)

def create_account(request):
	if request.method == "POST":
		data = urllib.parse.urlencode((request.POST).dict()).encode('utf-8')
		req = urllib.request.Request('http://models-api:8000/api/v1/profiles/create', data)
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		try:
			resp = json.loads(resp_json)
		except ObjectDoesNotExist:
			return JsonResponse("Cannot create profile", safe=False)
		auth = urllib.parse.urlencode({"name": resp['name']}).encode('utf-8')
		req = urllib.request.Request('http://models-api:8000/api/v1/auth/create', auth)
		try:
			resp2 = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
		except ObjectDoesNotExist:
			return JsonResponse("Cannot create authenticator", safe=False)
		return JsonResponse(resp2, safe=False)
	else:
		return JsonResponse("Must Post", safe=False)

def getAuthUser(request):
    post_data = request.POST.dict()
    resp = requestPost('auth_user/', post_data)
    auth_valid = True
    if resp['ok']:
        authenticator = resp['result']['auth']
        if authenticator['date_created'] < (timezone.now() - datetime.timedelta(days=1)).isoformat():
            auth_valid = False
    else:
        auth_valid = False
    if auth_valid:
        name = resp['result']['user']['name']
        result = {'result': name, 'ok': True}
    else:
        result = {'result': 'Invalid authenticator', 'ok': False}
    return JsonResponse(result)

def authenticate(request, authenticator):
	try:
		req = urllib.request.Request('http://models-api:8000/api/v1/auth/' + str(authenticator))
	except e:
		return JsonResponse("Authenticate failed.", safe=False)	
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
		#return JsonResponse("Authenticate failed.", safe=False)
	return JsonResponse(resp)	

def requestPost(url, postdata):
    post_data = urllib.parse.urlencode(postdata).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/' + url, data=post_data, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(resp_json)

def requestGet(url):
    req = urllib.request.Request('http://models-api:8000/api/v1/' + url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(resp_json)
########################################









