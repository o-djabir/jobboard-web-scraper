from webScraper.models import Offre
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

def job_list(request):
    jobs = Offre.objects.all()
    context = {
        'job_list': jobs
    }
    return render(request, "webScraper/job_list.html", context)

def delete_offre(request, *args, **kwargs):
    offre_id = kwargs["id"]
    try:
        query = Offre.objects.get(id = offre_id)
        query.delete()
        return HttpResponseRedirect('/webScraper/')
    except:
        return HttpResponseNotFound()
    
    
    


# Create your views here.
