from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> Store Front</h1>")
