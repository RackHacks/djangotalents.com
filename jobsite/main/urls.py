from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^contact/?$', 'contact', name='contact'),
    url(r'^accounts/register/?$', 'signup',
        {'backend': 'registration.backends.default.DefaultBackend'},
        name='signup'),
    url(r'^accounts/login/?$', 'login', name='login'),
    url(r'^accounts/logout/?$', 'logout', name='logout'),
    url(r'^seekers/?$', 'seekers', name='seekers'),
    url(r'^talents/?$', 'talents', name='talents'),
    url(r'^talents/(?P<iso>\w{2})/?$', 'talents_by_country', name='talents_by_country'),
    url(r'^talent/(?P<username>[\w.@+-]+)/?$', 'talent', name='talent'),
    url(r'^talent/(?P<username>[\w.@+-]+)/contact/?$', 'talent_contact', name='talent_contact'),
    url(r'^terms_of_service/$', 'terms_of_service', name='terms'),
    url(r'^profile/$', 'profile', name='profile'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)