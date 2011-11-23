from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^contact/?$', 'contact', name='contact'),
    url(r'^accounts/register/?$', 'signup',
        {'backend': 'registration.backends.default.DefaultBackend'},
        name='signup'),
    url(r'^accounts/login/?$', 'login', name='login'),
    url(r'^seekers/?$', 'seekers', name='seekers'),
    url(r'^talent/?$', 'talent', name='talent'),
    url(r'^terms_of_service/$', 'terms_of_service', name='terms'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)