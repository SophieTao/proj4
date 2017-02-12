from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import hashers
from django.forms.models import model_to_dict
from django import db
from profiles import models
from django.core import serializers
from django.db.models import Q
from .models import Profile
from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class IndexView(generic.ListView):
		template_name = 'home.html'
		context_object_name = 'all_users'

		def get_queryset(self):
				return Profile.objects.all()
# def home(request):
# 	context = {}
# 	template = 'home.html'
# 	return render(request, template, context)

def create_profile(request):
	if request.method != 'POST':
		return JsonResponse("Must make POST request.", safe=False)
	if 'name' not in request.POST:
		return JsonResponse("Missing required fields.", safe=False)
	profile = Profile(name=request.POST['name'])
	try:
		profile.save()
	except db.Error:
		return JsonResponse(str(db.Error), safe=False)
	return JsonResponse({'profile_id': profile.pk}, safe=False)

def retrieve_profile(request, profile_id):
    if request.method != 'GET':
        return JsonResponse(request, "Must make GET request.",safe=False)
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        return JsonResponse(request, "Profile not found.",safe=False)

    return JsonResponse({'name': profile.name},safe=False)



# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import profile
# from .serializers import ProfileSerializer

# # def home(request):
# # 	context = {}
# # 	template = 'home.html'
# # 	return render(request, template, context)



# #lists all stocks or create a new one
# #stocks/
# class ProfileList(APIView):

# 	def get(self, request):
# 		profiles =profile.objects.all();
# 		serializer = ProfileSerializer(profiles, many=True) #many: many json objects
# 		return Response(serializer.data) #return json data

# 	def post(self):
# 			pass