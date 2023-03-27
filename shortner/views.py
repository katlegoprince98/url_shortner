from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')

def create(request, pk):
    if request.method == "POST":
        link = request.POST['link']
        link_id = str(uuid.uuid4())[:5]
        new_url = Url(link=link, link_id=link_id)
        new_url.save()
        link_id = Url.objects.get(pk = link_id)
        return render(request, 'create.html', {
            "code": link_id
        })

        