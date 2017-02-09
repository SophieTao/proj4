from django.shortcuts import render

def meal(request):
	context = {}
	template = 'meal.html'
	return render(request, template, context)
