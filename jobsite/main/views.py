from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import send_mail

from main.forms import ContactForm


def index(request):
    return render_to_response('index.html', RequestContext(request))

def about(request):
    return render_to_response('about.html', RequestContext(request))

def contact(request):
    success =  False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['sender'],
                ['djangotalents@codenga.com'],
            )
            success = True
            form = ContactForm()
    return render_to_response('contact.html', RequestContext(request, {
        'form': form,
        'success': success,
    }))

def signup(request):
    return render_to_response('signup.html', RequestContext(request))

def seekers(request):
    return render_to_response('seekers.html', RequestContext(request))

def talent(request):
    return render_to_response('talent.html', RequestContext(request))