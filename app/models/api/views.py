from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Cafe, Comment, Profile
from api import models
from django.http import JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect

class IndexView(generic.ListView):
		model = Cafe
		template_name = 'cafe_list.html'
		context_object_name = 'all_cafes'

		def get_queryset(self):
				return Cafe.objects.all()

class CafeCreate(generic.CreateView):
	model = Cafe  
	success_url = reverse_lazy('cafe_list')
	fields = ['name','location','date','description','Calories'] #fields from model.py

class CafeDelete(generic.DeleteView):
    model = Cafe
    success_url = reverse_lazy('cafe_list')

class CafeUpdate(generic.UpdateView):
		model = Cafe
		success_url = reverse_lazy('cafe_list')
		fields = ['name','location','date','description','Calories'] #fields from model.py

def retrieve_cafe(request, comment_id):
    if request.method != 'GET':
        return JsonResponse(request, "Must make GET request.",safe=False)
    c = Cafe.objects.get(pk=comment_id)
    return JsonResponse({'name': c.name,'location':c.location,'date':c.date,'description':c.description,'Calories':c.Calories})

def retrieve_cafe_all(request):
		if request.method != 'GET':
			return JsonResponse(request, "Must make GET request.",safe=False) 
		meals = Cafe.objects.all()
		response = []
		for meal in meals:
			response.append({"name": meal.name,"location": meal.location,"date": meal.date,"description": meal.description,"Calories": meal.Calories,})
		return JsonResponse({"data": response})

class CommentIndexView(generic.ListView):
		model = Comment
		template_name = 'comment.html'
		context_object_name = 'all_comments'

		def get_queryset(self):
				return Comment.objects.all()

class CommentCreate(generic.CreateView):
	model = Comment  
	success_url = reverse_lazy('comment_list')
	fields = ['description','feedback','author','date_written','rating','meal'] #fields from model.py

class CommentDelete(generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')

class CommentUpdate(generic.UpdateView):
		model = Comment
		success_url = reverse_lazy('comment_list')
		#fields = ['description','feedback','author','date_written','rating','meal'] #fields from model.py
		fields = ['description','feedback','date_written','rating'] #fields from model.py

def retrieve_comment(request, comment_id):
    if request.method != 'GET':
        return JsonResponse(request, "Must make GET request.",safe=False)
    c = Comment.objects.get(pk=comment_id)
    return JsonResponse({'description': c.description,'feedback':c.feedback,'date_written':c.date_written,'rating':c.rating})

class ProfileIndexView(generic.ListView):
		template_name = 'home.html'
		context_object_name = 'all_users'

		def get_queryset(self):
				return Profile.objects.all()

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

