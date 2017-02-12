from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import comment 
from django.http import JsonResponse
from django.contrib.auth import hashers
from django.forms.models import model_to_dict
from django import db
from comments import models
from django.core import serializers
from django.db.models import Q

class IndexView(generic.ListView):
		template_name = 'comment.html'
		context_object_name = 'all_comments'

		def get_queryset(self):
				return comment.objects.all()

# class DetailView(generic.DetailView):
# 		model = comment			
# 		template_name	= 'detail.html'
# 		def get_queryset(self):
# 			return JsonResponse({'comment': model.description},safe=False)
def retrieve_profile(request, comment_id):
    if request.method != 'GET':
        return JsonResponse(request, "Must make GET request.",safe=False)
    try:
        c = comment.objects.get(pk=comment_id)
    except comment.DoesNotExist:
        return JsonResponse(request, "Comment not found.",safe=False)

    return JsonResponse({'description': c.description},safe=False)

class CommentCreate(CreateView):
		model = comment
		fields = ['description'] #fields from model.py


# from django.conf import settings
# from .forms import commentForm
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from django.contrib.auth import hashers
# from django.forms.models import model_to_dict
# from django import db
# from profiles import models
# from django.core import serializers
# from django.db.models import Q
# from .models import comment

# def comment(request):
# 	form = commentForm(request.POST or None)
# 	confirm_message = None
# 	if form.is_valid():
# 		print(request_POST)
		
# 	context = locals()
# 	template = 'comment.html'
# 	return render(request, template, context)

# def create_comment(request):
# 	if request.method != 'POST':
# 		return JsonResponse("Must make POST request.", safe=False)
# 	if 'description' not in request.POST:
# 		return JsonResponse("Missing required fields.", safe=False)
# 	comment = comment(description=request.POST['description'])
# 	try:
# 		comment.save()
# 	except db.Error:
# 		return JsonResponse(str(db.Error), safe=False)
# 	return JsonResponse({'comment_id': comment.pk}, safe=False)
