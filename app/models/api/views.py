from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.views import generic 
import hmac
import os
from django.contrib.auth import hashers
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.forms.models import model_to_dict
from api import models
from json import dumps
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from .forms import *
from models import settings
import datetime

'''
Check password, create/delete/get authenticator
'''
# def check_user_password(request):
# 	email_addr = request.POST.get('email')
# 	password = request.POST.get('password')
# 	found_profile = True
# 	try:
# 		user = Profile.objects.get(email=email_addr)
# 	except ObjectDoesNotExist:
# 		found_profile = False
# 	resp = {}
# 	if (found_profile and hashers.check_password(password, user.password)):
# 		resp['ok'] = True
# 		resp['result'] = model_to_dict(user)
# 	else:
# 		resp['ok'] = False
# 		resp['result'] = "Invalid email or password"
# 	return JsonResponse(resp)

def createAuth(request):
	if request.method == 'POST':
		try:
			u = Profile.objects.get(username = request.POST['username'])
		except Profile.DoesNotExist:
			return JsonResponse("User Does Not Exist",safe=False)
		if not hashers.check_password(request.POST["password"], u.password):
			return JsonResponse("Incorrect password", safe=False)	
		#	Check if the newly generated authenticator already exists in the database
		try: 
			user = Authenticator.objects.get(user_id=u.pk)
			deleteAuth(request,user.authenticator)
		except Authenticator.DoesNotExist:
			pass
		auth_hash = hmac.new(key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
		auth = Authenticator.objects.create(date_created = datetime.datetime.now(), user_id = u.pk, authenticator=auth_hash)
		try:
			auth.save()
			resp=model_to_dict(auth)
			return JsonResponse(resp)
			#resp['ok'] = True
			#resp["result"] = {"authenticator": model_to_dict(auth)}
		except KeyError:
			#resp['ok'] = False
			return JsonResponse("Failed to create authenticator", safe=False)
	else:
		return JsonResponse("Must Post",safe=False)		

# def getAuth(request, authenticator):
# 	if request.method == 'GET':
# 		try:
# 			authenticator = Authenticator.objects.filter(pk=authenticator)
# 		except ObjectDoesNotExist:
# 			return JsonResponse("User has not  been authenticated yet.",safe=False)
# 		# auth = Authenticator.objects.filter(user_id=pk)
# 		alist = []
# 		for i in auth:
# 			alist.append(model_to_dict(i))
# 			return JsonResponse(alist, safe=False)
# 		return JsonResponse("User does not exist", safe=False)
# 	else:
# 		return JsonResponse("Must Get",safe=False)	

def deleteAuth(request,authenticator):
	try:
		authenticator = Authenticator.objects.get(pk=authenticator)
	except ObjectDoesNotExist:
		return JsonResponse("User has not  been authenticated yet.",safe=False)
	authenticator.delete()
	return JsonResponse("Successfully deleted user authentication",safe=False)

def checkAuth(request):
	try:
		user = Profile.objects.get(username = request.POST['username'])
	except ObjectDoesNotExist:
		return JsonResponse("Authenticator does not exist.",safe=False)
	except KeyError:
		try: 
			u = Authenticator.objects.get(pk = request.POST['authenticator'])
		except ObjectDoesNotExist:
			return JsonResponse("Authenticator does not exist.",safe=False)
		return JsonResponse( model_to_dict(u),safe=False)
	try:
		u = Authenticator.objects.get(user_id=user.pk)
	except ObjectDoesNotExist:
		return JsonResponse("Authenticator does not exist.",safe=False)
	except KeyError:
		return JsonResponse("Authenticator Does Not Exist",safe=False)
	try:
		pw = request.POST["password"];
	except KeyError:
		return JsonResponse("Incorrect password", safe=False)	
	if not hashers.check_password(request.POST["password"], user.password):
		return JsonResponse("Incorrect password", safe=False)	
	else:
		return JsonResponse( model_to_dict(u),safe=False)



def authView(request):
	auths = Authenticator.objects.all()
	response = []
	for auth in auths:
		response.append(model_to_dict(auth))
	return JsonResponse(response,safe=False)
	# try:
	# 	authenticator = Authenticator.objects.get(pk=request.POST['authenticator'])
	# except ObjectDoesNotExist:
	# 	return JsonResponse("Authenticator does not exist.",safe=False)
	# return JsonResponse( model_to_dict(authenticator),safe=False)



'''
Cafe (create, edit, delete, retrieve, IndexView)
'''

def indexView(request):
	if request.method == 'GET':
		result = {}
		try:
			result["ok"] = True
			result["result"] = [model_to_dict(cafe) for cafe in Cafe.objects.all()]
		except Exception:
			result["ok"] = False
			result["result"] = []
		return JsonResponse(result)
	else:
		return JsonResponse("Must Get",safe=False)		

def create_cafe(request):
	if request.method == 'POST':
		result = {}
		result_msg = None
		try:
			req_input = {
			'name': request.POST['name'],
			'location':request.POST['location'],
			'date':request.POST['date'],
			'description':request.POST['description'],
			'Calories':request.POST['Calories'],
			}
		except KeyError:
			req_input = {}
		form = CafeForm(req_input)
		if form.is_valid():
			cafe = form.save()
			result["ok"] = True
			result["result"] = {"id": cafe.id}
			return JsonResponse(req_input,safe=False)
		else:
			result_msg = "Input did not contain all the required fields."
			return JsonResponse(result_msg,safe=False)
	else:
		return JsonResponse("Must Post",safe=False)		

def delete_cafe(request, pk):
	if request.method == 'POST':
		resp = {}
		cafefound = True
		try:
			cafe = Cafe.objects.get(pk=pk)
			cafe.delete()
		except ObjectDoesNotExist:
			cafefound = False
			return JsonResponse("This meal does not exist.",safe=False)
		if cafefound:
			return JsonResponse("Deleted meal", safe=False)
	else:	
		return JsonResponse("Must Post",safe=False)		

'''
Comment (create, delete, commentView)
'''


def commentView(request):
	if request.method == 'GET':
		result = {}
		try:
			result["ok"] = True
			result["result"] = [model_to_dict(comment) for comment in Comment.objects.all()]
		except Exception:
			result["ok"] = False
			result["result"] = []
		return JsonResponse(result)
	else:
		return JsonResponse("Must Get",safe=False)		

def create_comment(request):
	if request.method == 'POST':		
		result = {}
		result_msg = None
		try:
			req_input = {
			'description': request.POST['description'],
			'feedback':request.POST['feedback'],
			'date_written':request.POST['date_written'],
			'rating':request.POST['rating'],
			}
		except KeyError:
			req_input = {}
			result_msg = "Input did not contain all the required fields."
		form = CommentForm(req_input)
		if form.is_valid():
			comment = form.save()
			return JsonResponse(req_input,safe=False)
		else:
			return JsonResponse(result_msg,safe=False)
	else:
		return JsonResponse("Must Post",safe=False)	

def delete_comment(request, pk):
	if request.method == 'POST':		
		resp = {}
		commentfound = True
		try:
			comment = Comment.objects.get(pk=pk)
			comment.delete()
		except ObjectDoesNotExist:
			commentfound = False
			return JsonResponse("This comment does not exist.",safe=False)
		if commentfound:
			return JsonResponse("Deleted comment ", safe=False)
	else:
		return JsonResponse("Must Post",safe=False)	

'''
Profile (create, retrieve, IndexView)
'''

def profileView(request):
	if request.method == 'GET':			
		result = {}
		try:
			result["ok"] = True
			result["result"] = [model_to_dict(profile) for profile in Profile.objects.all()]
		except Exception:
			result["ok"] = False
			result["result"] = []
		return JsonResponse(result)
	else:
		return JsonResponse("Must Get",safe=False)	


def create_profile(request):
	if request.method == 'POST':
		user = Profile()
		try:
			u = Profile.objects.get(username=request.POST['username'])
		except ObjectDoesNotExist:
			try:
				v = Profile.objects.get(username=request.POST['email'])
			except ObjectDoesNotExist:
				try:
					user.username = request.POST['username']
					user.email = request.POST['email']
					user.password = hashers.make_password(request.POST['password'])
				except KeyError:
					return JsonResponse("Input did not contain all the required fields.",safe=False)
				user.save()
				return JsonResponse(model_to_dict(user))
			return JsonResponse("unique",safe=False)
		return JsonResponse("unique2",safe=False)
	else:
		return JsonResponse("Must Post",safe=False)


def delete_profile(request, pk):
	if request.method == 'POST':	
		resp = {}
		profilefound = True
		try:
			profile = Profile.objects.get(pk=pk)
			profile.delete()
		except ObjectDoesNotExist:
			profilefound = False
			return JsonResponse("This profile does not exist.",safe=False)
		if profilefound:
			return JsonResponse("Deleted profile ", safe=False)
	else:
		return JsonResponse("Must Post",safe=False)	

def retrieve_profile(request):
	if request.method == 'POST':
		try:
			profile = Profile.objects.get(username=request.POST['username'])
			p = [model_to_dict(profile)];
			#return JsonResponse(model_to_dict(profile))
		except ObjectDoesNotExist:
			return JsonResponse("Profile does not exist.",safe=False)
		if hashers.check_password(request.POST["password"], model_to_dict(profile)["password"]):
			return JsonResponse(model_to_dict(profile))			
		else:
			return JsonResponse("Incorrect Password", safe=False)
		
	else:
		return JsonResponse("Must Post",safe=False)


def get_recent_meals(request):
    if request.method == 'GET':
        recent_meals = Cafe.objects.order_by('-date')[:3]
        meallist = []
        for i in recent_meals:
            meallist.append(model_to_dict(i))
        return JsonResponse(meallist, safe=False)
    else:
        return JsonResponse("Must make GET request.",safe=False)

def retrieve_cafe_all(request):
		if request.method != 'GET':
			return JsonResponse("Must make GET request.",safe=False) 
		meals = Cafe.objects.all()
		response = []
		for meal in meals:
			response.append(model_to_dict(meal))
		return JsonResponse(response,safe=False)
	
def retrieve_comment_all(request):
		if request.method == 'GET':
				comments = Comment.objects.all()
				commentlist = []
				for i in comments:
					commentlist.append(model_to_dict(i))
				return JsonResponse(commentlist, safe=False)
		else:
				return JsonResponse("Must make GET request.",safe=False)

'''
Retrieve and Update Cafe, Comment, Profile
'''
class CafeRetrieveUpdate(View):

	def get(self, request, pk):
		result = {}
		try:
			cafe = Cafe.objects.get(pk=pk)
			return JsonResponse(model_to_dict(cafe))
		except ObjectDoesNotExist:
			return JsonResponse("Cafe does not exist.",safe=False)

	def post(self, request, pk):
		result = {}
		try:
			cafe = Cafe.objects.get(pk=pk)
			cafe_fields = [c.name for c in Cafe._meta.get_fields()]
			for field in cafe_fields:
				if field in request.POST:
					setattr(cafe, field, request.POST[field])
			cafe.save()
			return JsonResponse(model_to_dict(cafe))			
		except ObjectDoesNotExist:
			return JsonResponse("Cafe does not exist.",safe=False)

class CommentRetrieveUpdate(View):
	def get(self, request, pk):
		result = {}
		try:
			comment = Comment.objects.get(pk=pk)
			return JsonResponse(model_to_dict(comment))
		except ObjectDoesNotExist:
			return JsonResponse("Comment does not exist.",safe=False)

	def post(self, request, pk):
		result = {}
		try:
			comment = Comment.objects.get(pk=pk)
			comment_fields = [c_field.name for c_field in Comment._meta.get_fields()]
			for field in comment_fields:
				if field in request.POST:
					setattr(comment, field, request.POST[field])
			comment.save()
			return JsonResponse(model_to_dict(comment))			
		except ObjectDoesNotExist:
			return JsonResponse("Comment does not exist.",safe=False)

class ProfileRetrieveUpdate(View):
	def get(self, request, pk):
		try:
			profile = Profile.objects.get(pk=pk)
			if hashers.check_password(request.POST['password'], profile.password):
				return JsonResponse(model_to_dict(profile))			
		except ObjectDoesNotExist:
			return JsonResponse("Profile does not exist.",safe=False)

	def post(self, request, pk):
		result = {}
		try:
			profile = Profile.objects.get(pk=pk)
			profile_fields = [p_field.username for p_field in Profile._meta.get_fields()]
			for field in profile_fields:
				if field in request.POST:
					setattr(profile, field, request.POST[field])
			profile.save()
			return JsonResponse(model_to_dict(profile))			
		except ObjectDoesNotExist:
			return JsonResponse("Profile does not exist.",safe=False)

