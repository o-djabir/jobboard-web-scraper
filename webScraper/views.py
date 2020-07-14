from django.http import HttpResponse

def index(request):
    return HttpResponse("I'm not quite sure what is going on, but I'll find out")

def index2(request):
    return HttpResponse("Ok, MAYBE, just MAYBE, I'm starting to get it a little ")
    
# Create your views here.
