from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from home.models import *
import requests
import os
import json
from django.contrib.auth.decorators import login_required
from website.settings import GOOGLE_PLUS_KEY

# Create your views here.
def index(request):
    r = requests.get('https://www.googleapis.com/plus/v1/people/111490187039594096525/activities/public?key={0}&maxResults=3'.format( GOOGLE_PLUS_KEY ))

    return render_to_response('index.html', {'events': r.json(), 'request': request})

def about(request):
    return render_to_response('about.html', {'request': request})

def sponsors(request):
    sponsors = Sponsor.objects.all().order_by('name')

    platinum_sponsors = sponsors.filter(sponsorship_level='platinum')
    gold_sponsors = sponsors.filter(sponsorship_level='gold')
    silver_sponsors = sponsors.filter(sponsorship_level='silver')

    return render_to_response('sponsor.html', {
        'sponsors': sponsors,
        'request': request,
        'platinum_sponsors': platinum_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        })

def calendar(request):
    return render_to_response('calendar.html', {'request': request})

def events(request):
    r = requests.get('https://www.googleapis.com/plus/v1/people/111490187039594096525/activities/public?key={0}&maxResults=10'.format( GOOGLE_PLUS_KEY ))

    return render_to_response('events.html', {'events': r.json(), 'request': request})

@login_required(login_url='/login/')
def event_admin(request):
    print("USER:  ", request.user)

    return render_to_response('event_admin.html', {})

def officers(request):
    users = []
    return render_to_response('officers.html', {'users': users})

def wais(request):
    return render_to_response('wais.html')

def twitter(request):
    return render(request, 'twitter.html')

def newsletter_home(request):
    return render(request, 'newsletter.html')

def newsletter(request, id):
    nid = 'newsletters/{0}.html'.format(id)
    return render( request, 'newsletter.html', {'newsletter_file': nid})


def error500(request):
    return render_to_response('500.html')