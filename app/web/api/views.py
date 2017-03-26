from django.shortcuts import render, redirect
from django.core import serializers
from .forms import CreateAccountForm, CreateListingForm, LoginForm
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages 
import urllib
import urllib.request
import urllib.parse
import json

def home(request):
    req = urllib.request.Request('http://exp-api:8000/home/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)  
    # return JsonResponse(resp[0],safe=False)
    context = {'meals': resp[0],'allcomments': resp[1]}
    # return JsonResponse(context,safe=False)
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
		n = request.GET.get('next') or reverse('home')
		form = LoginForm()
		#return JsonResponse("get",safe=False)	
		return render(request, 'api/login.html', {'form': form, 'next': n})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if not form.is_valid():
			return JsonResponse("invalid input",safe=False)	
		n = form.cleaned_data.get('next') or reverse('home')
		post = urllib.parse.urlencode(form.cleaned_data).encode('utf-8')
		req = urllib.request.Request('http://exp-api:8000/login', post)
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		resp = json.loads(resp_json)
		# return JsonResponse(resp==, safe=False);
		if resp == "User Does Not Exist":
			response = HttpResponseRedirect(reverse('login'))
			return response    
		req2 = urllib.request.Request('http://exp-api:8000/auth/check',post)
		resp2 = json.loads(urllib.request.urlopen(req2).read().decode('utf-8'))
		if resp2 == "Authenticator does not exist.":
			req3 = urllib.request.Request('http://exp-api:8000/auth/check',post)
			resp3 = json.loads(urllib.request.urlopen(req3).read().decode('utf-8'))
		#return JsonResponse("Authenticate failed.", safe=False)
		authenticator = resp['authenticator']
		#return JsonResponse(resp['authenticator'], safe=False);
		response = HttpResponseRedirect(n)
		# response.delete_cookie("authenticator")
		response.set_cookie("authenticator", authenticator)
		return response

def logout(request):
    auth = request.COOKIES.get('authenticator')
    # return JsonResponse(auth, safe=False);
    #post = urllib.parse.urlencode({"authenticator": auth}).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/logout/'+str(auth))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie("authenticator")
    return response		

def create_listing(request):
	auth = request.COOKIES.get('authenticator')			

	if not auth:
		return HttpResponseRedirect(reverse("login") + "?next=" + reverse('create_listing'))
	if request.method == 'POST':
		form = CreateListingForm(request.POST)
		if form.is_valid():
			#return JsonResponse(request.POST.dict(), safe=False)
			#data = {"authenticator": auth};
			data = request.POST.dict()
			data['authenticator'] = auth
			#c = {x: data.get(x, 0) + jsondata.get(x, 0) for x in set(data).union(jsondata)}
			#c = {**data, **jsondata}
			#c.update(data)

			post = urllib.parse.urlencode(data).encode('utf-8')
			try:
				req = urllib.request.Request('http://exp-api:8000/listing/create', data=post, method='POST')
			except ObjectDoesNotExist:
				return JsonResponse("Fail to create a new listing", safe=False)
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)
			#return JsonResponse(resp, safe=False)
			# if not resp[0]:
			# 	return JsonResponse("error0", safe=False)
			# 	errors = resp[1]
			# 	if resp[1] == "ERROR: Invalid Auth":
			# 		return JsonResponse("error3", safe=False)
			# 		return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
			# else:
			return HttpResponseRedirect(reverse('home'))
		else:
			return JsonResponse("Invalid input", safe=False)
	else:
		form = CreateListingForm()
	return render(request, 'api/create_listing.html', {'form': form})



def create_account(request):
	# auth = request.COOKIES.get("authenticator")
	# return JsonResponse(auth, safe=False)
	# if auth:
	# 	return HttpResponseRedirect(reverse('home'))
	if request.method == 'GET':
		form = CreateAccountForm()
		return render(request, 'api/create_account.html', {'form': form})
	form = CreateAccountForm(request.POST)
	if not form.is_valid():
		# return JsonResponse("invalid form",safe=False)
		# messages.error(request, "Error")
		return render(request, 'api/create_account.html', {'form': form})
	username = form.cleaned_data['username']
	email = form.cleaned_data['email']
	password = form.cleaned_data['password']
	post_data = {'username': username,
				 'email': email,
				 'password': password,}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	try:
		req = urllib.request.Request('http://exp-api:8000/create_account', data=post_encoded)
	except ObjectDoesNotExist:
		return JsonResponse("Fail to signup", safe=False)
		return render(request, 'api/create_account.html', {'form': form})
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	# return JsonResponse(resp,safe=False)		
	#post_data = {'name': username,'email': email, 'password': password}
	#post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	# try:
	# 	req2 = urllib.request.Request('http://exp-api:8000/login/', data=post_encoded, method='POST')
	# except ObjectDoesNotExist:
	# 	return JsonResponse("Created a new account but failed to login", safe=False)
	# 	return render(request, 'api/login.html', {'form': form})
	return render(request, 'api/login.html', {'form': form})
	# resp_json = urllib.request.urlopen(req2).read().decode('utf-8')
	# resp = json.loads(resp_json)
	# authenticator = resp['result']['authenticator']
	# response = HttpResponseRedirect(reverse('index'))
	# response.set_cookie("auth", authenticator["authenticator"])
	# return response

	