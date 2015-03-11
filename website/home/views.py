from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings

# Create your views here.
def index(request):
    return render_to_response('index.html', {})

def about(request):
    return render_to_response('about.html', {})

def sponsors(request):
    return render_to_response('sponsor.html', {})