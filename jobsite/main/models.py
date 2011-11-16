from django.contrib.auth.models import User
from django.db import models


JOB_CHOICES = (
    (u'N', u'Not right now'),
    (u'F', u'Freelancer'),
    (u'U', u'Fulltime'),
    (u'B', u'Fulltime/Freelancer'),
)

class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', related_name='+')
    #country
    bio = models.TextField()
    looking_for_a_job = models.CharField(max_length=1, choices=JOB_CHOICES)

    def __unicode__(self):
        return self.get_full_name()

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def get_full_name(self):
        return self.user.get_full_name()

class Link(models.Model):
    user = models.ForeignKey(UserProfile, related_name='links')
    name = models.CharField(max_length=50)
    url = models.URLField()

def get_profile(user):
    profile, created = UserProfile.objects.get_or_create(
        user=user,
    )
    return profile
