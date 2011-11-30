from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from countries.models import Country

JOB_CHOICES = (
    (u'N', u'Not right now'),
    (u'F', u'Freelance'),
    (u'U', u'Fulltime'),
    (u'B', u'Fulltime/Freelance'),
)

User._meta.get_field('email')._unique = True
User._meta.get_field('email').null = False
User._meta.get_field('email').blank = False
User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', related_name='+')
    bio = models.TextField()
    looking_for_a_job = models.CharField(max_length=1, choices=JOB_CHOICES)
    country = models.ForeignKey(Country, related_name='users')
    location = models.CharField(max_length=150)
    github = models.CharField('Github Username', max_length=50, null=True, blank=True)
    facebook = models.CharField('Facebook Username', max_length=50, null=True, blank=True)
    twitter = models.CharField('Twitter Username', max_length=50, null=True, blank=True)
    gtalk = models.CharField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    msn = models.EmailField(null=True, blank=True)
    yahoo = models.EmailField(null=True, blank=True)
    aim = models.CharField(max_length=150, null=True, blank=True)
    jabber = models.CharField(max_length=150, null=True, blank=True)
    irc = models.CharField(max_length=150, null=True, blank=True)
    blog = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.get_full_name()

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def get_full_name(self):
        return self.user.get_full_name()

    def get_display(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else self.username

class Link(models.Model):
    user = models.ForeignKey(UserProfile, related_name='portfolio')
    name = models.CharField(max_length=50)
    url = models.URLField()

def get_profile(user):
    profile, created = UserProfile.objects.get_or_create(
        user=user,
    )
    return profile
User.get_profile = get_profile

def get_non_empty_countries():
    return Country.objects.annotate(users_count=Count('users')).filter(users_count__gt=0)