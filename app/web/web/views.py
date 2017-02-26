# from django.shortcuts import render, redirect
# import urllib
# import urllib.request
# import urllib.parse
# import json
# from django.http import JsonResponse
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# import re
# from django.core.urlresolvers import reverse

# def index(request):
#     req = urllib.request.Request('http://exp-api:8000/api/v1/home')

#     template = loader.get_template('web/index.html')
#     resp_json = urllib.request.urlopen(req).read().decode('utf-8')
#     resp = json.loads(resp_json)
#     context = resp["resp"]
#     return HttpResponse(template.render(context, request))



# # from django.views import generic 
# # from django.views.generic.edit import CreateView, UpdateView, DeleteView
# # from django.core.urlresolvers import reverse_lazy
# # #from .models import Cafe, Comment, Profile
# # from django.http import JsonResponse,HttpResponseRedirect
# # from django.core import serializers
# # from django.shortcuts import render, redirect

# # def index(request):
# # 	return render(request, 'index.html', {})

# # class IndexView(generic.ListView):
# # 		template_name = 'index.html'

# # 	