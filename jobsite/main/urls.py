from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^contact/?$', 'contact', name='contact'),
    url(r'^accounts/register/?$', 'signup',
        {'backend': 'registration.backends.default.DefaultBackend'},
        name='signup'),
    url(r'^seekers/?$', 'seekers', name='seekers'),
    url(r'^talent/?$', 'talent', name='talent'),
)
