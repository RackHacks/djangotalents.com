from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.core.urlresolvers import reverse
from registration.backends import get_backend
from countries.models import Country
from main.forms import ContactForm, UserForm, SignupForm, EditUserForm, UserProfileForm
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
            form.send()
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

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('talents'))

    if request.method == 'POST':
        auth_form = AuthenticationForm(None, request.POST)
        if auth_form.is_valid():
            if not request.POST.get('remember_me', None):
                request.session.set_expiry(0)
            auth_login(request, auth_form.get_user())

    return HttpResponseRedirect(reverse('index'))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def seekers(request):
    return render_to_response('seekers.html', RequestContext(request))

def talents(request):
    countries = get_non_empty_countries
    return render_to_response('talents.html', RequestContext(request, {
        'countries': countries,
    }))

def talents_by_country(request, iso):
    country = get_object_or_404(Country, iso__iexact=iso)
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

def talent_contact(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    form = ContactForm()
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send(recipient=profile.user.email)
            success = True
            form = ContactForm()
    return render_to_response('talent_contact.html', RequestContext(request, {
        'profile': profile,
        'form': form,
        'success': success,
    }))

def terms_of_service(request):
    pass

@login_required
def profile(request):
    user_form = EditUserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.get_profile())
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.get_profile())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('talent', request.user.username)
    return render_to_response('profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    }, RequestContext(request))