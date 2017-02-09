from django.shortcuts import render

def comment(request):
	context = {}
	template = 'comment.html'
	return render(request, template, context)
