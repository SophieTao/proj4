from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Comment 
from django.http import JsonResponse
from comments import models
from django.core import serializers
from .forms import commentForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
		model = Comment
		template_name = 'commentt.html'
		context_object_name = 'all_comments'

		def get_queryset(self):
				return Comment.objects.all()

class DetailView(generic.DetailView):
		model = Comment			
		template_name	= 'detail.html'

class CommentCreate(generic.CreateView):
	model = Comment  
	success_url = reverse_lazy('comment_list')
	fields = ['description']
	#fields = ['description','feedback','author','date_written','rating','meal'] #fields from model.py

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')

class CommentUpdate(UpdateView):
		model = Comment
		fields = ['description','feedback','author','date_written','rating','meal'] #fields from model.py

def retrieve_comment(request, comment_id):
    if request.method != 'GET':
        return JsonResponse(request, "Must make GET request.",safe=False)
    c = Comment.objects.get(pk=comment_id)
    return JsonResponse({'description': c.description,'feedback':c.feedback,'author':c.author,'date_written':c.date_written,'rating':c.rating,'meal':c.meal},safe=False)

