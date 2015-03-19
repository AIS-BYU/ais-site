from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from home.models import *
import requests
import json

# Create your views here.
def index(request):
    r = requests.get('https://www.googleapis.com/plus/v1/people/111490187039594096525/activities/public?key=AIzaSyCsZyECtnoQw2xKqlBWRs13v0_DUrC5Q5I&maxResults=3')

    return render_to_response('index.html', {'events': r.json()})

def about(request):
    return render_to_response('about.html', {})

def sponsors(request):
    sponsors = Sponsor.objects.all().order_by('name')

    return render_to_response('sponsor.html', {'sponsors': sponsors})