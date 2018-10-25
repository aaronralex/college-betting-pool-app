from django.http import HttpResponse

def index(request):
	return HttpResponse("The start of something great by the Super Software Bros.")
