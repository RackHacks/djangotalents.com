from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import send_mail
from registration.backends import get_backend
from countries.models import Country

from main.forms import ContactForm, UserForm, SignupForm
from main.models import UserProfile, get_non_empty_countries


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

def signup(request, backend, success_url=None, extra_context=None):
    disallowed_url = 'registration_disallowed'
    backend = get_backend(backend)

    if not backend.registration_allowed(request):
        return redirect(disallowed_url)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        signup_form = SignupForm(request.POST)

        if user_form.is_valid() and signup_form.is_valid():
            new_user = backend.register(request, **user_form.cleaned_data)
            profile = signup_form.save(commit=False)
            profile.user = new_user
            profile.save()
            if success_url is None:
                to, args, kwargs = backend.post_registration_redirect(request, new_user)
                return redirect(to, *args, **kwargs)
            else:
                return redirect(success_url)
    else:
        user_form = UserForm()
        signup_form = SignupForm()
    
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(
        'signup.html',
        {
            'user_form': user_form,
            'signup_form': signup_form
        },
        context_instance=context)

def seekers(request):
    return render_to_response('seekers.html', RequestContext(request))

def talents(request):
    countries = get_non_empty_countries
    return render_to_response('talents.html', RequestContext(request, {
        'countries': countries,
    }))

def talents_by_country(request, country):
    country = get_object_or_404(Country, name=country.upper)
    profiles = country.users.all()
    return render_to_response('talents_by_country.html', RequestContext(request, {
        'profiles': profiles,
        'country': country.name.capitalize
    }))

def talent(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    return render_to_response('talent.html', RequestContext(request, {
        'profile': profile,
    }))

def terms_of_service(request):
    pass
