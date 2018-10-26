from django.http import HttpResponse
from django.template import loader

def index(request):
	#return HttpResponse("The start of something great by the Super Software Bros.")
	template = loader.get_template('collegebettingpool/home_page.html')
	context = {

	}
	return HttpResponse(template.render(context, request))
