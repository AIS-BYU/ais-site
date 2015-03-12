from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from home.models import *

# Create your views here.
def index(request):
    return render_to_response('index.html', {})

def about(request):
    return render_to_response('about.html', {})

def sponsors(request):
    sponsors = Sponsor.objects.all()

    return render_to_response('sponsor.html', {'sponsors': sponsors})