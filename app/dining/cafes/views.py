from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Cafe 
from django.http import JsonResponse,HttpResponseRedirect
from cafes import models
from django.core import serializers
from django.shortcuts import render, redirect

class IndexView(generic.ListView):
		model = Cafe
		template_name = 'cafe.html'
		context_object_name = 'all_cafes'

		def get_queryset(self):
				return Cafe.objects.all()

class DetailView(generic.DetailView):
		model = Cafe			
		template_name	= 'detail.html'

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