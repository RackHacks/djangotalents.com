from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', RequestContext(request))

def about(request):
    return render_to_response('about.html', RequestContext(request))

def contact(request):
    return render_to_response('contact.html', RequestContext(request))

def signup(request):
    return render_to_response('signup.html', RequestContext(request))

def seekers(request):
    return render_to_response('seekers.html', RequestContext(request))

def talent(request):
    return render_to_response('talent.html', RequestContext(request))