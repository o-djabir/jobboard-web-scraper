from webScraper.models import Offre
from django.shortcuts import render

def job_list(request):
    jobs = Offre.objects.all()
    context = {
        'job_list': jobs
    }
    return render(request, "webScraper/job_list.html", context)
    
# Create your views here.
