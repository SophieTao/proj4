from django.views.generic import View
from django.views import generic 
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.forms.models import model_to_dict
from api import models
from json import dumps
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from .forms import *

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
			user.name = request.POST['name']
		except KeyError:
			return JsonResponse("Input did not contain all the required fields.",safe=False)
		user.save()
		return JsonResponse(model_to_dict(user))
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
			return JsonResponse("This meal does not exist.",safe=False)
		if profilefound:
			return JsonResponse("Deleted profile ", safe=False)
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
		result = {}
		try:
			profile = Profile.objects.get(pk=pk)
			return JsonResponse(model_to_dict(profile))			
		except ObjectDoesNotExist:
			return JsonResponse("Profile does not exist.",safe=False)

	def post(self, request, pk):
		result = {}
		try:
			profile = Profile.objects.get(pk=pk)
			profile_fields = [p_field.name for p_field in Profile._meta.get_fields()]
			for field in profile_fields:
				if field in request.POST:
					setattr(profile, field, request.POST[field])
			profile.save()
			return JsonResponse(model_to_dict(profile))			
		except ObjectDoesNotExist:
			return JsonResponse("Profile does not exist.",safe=False)

