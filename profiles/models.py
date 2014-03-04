from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    degree_programme = models.CharField(max_length=255)
    year = models.IntegerField()
    compsoc_member = models.BooleanField()
    bio = models.TextField()

    def __unicode__(self):
        return '{0} {1} ({2})'.format(self.user.first_name, self.user.last_name, self.user.username)

class Skill(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    level = models.IntegerField()

    def __unicode__(self):
        return '{0} {1} ({2}) - {3}'.format(self.profile.user.first_name, self.profile.user.last_name,
                                            self.profile.user.username, self.name)


class ExternalPlace(models.Model):
    profile = models.ForeignKey(Profile)
    type = models.CharField(max_length=20)
    url = models.URLField()

    def __unicode__(self):
        return '{0} {1} ({2}) - {3}'.format(self.profile.user.first_name, self.profile.user.last_name,
                                            self.profile.user.username, self.type)