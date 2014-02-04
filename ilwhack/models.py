from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    name = models.CharField(max_length=64)
    nav_name = models.CharField(max_length=128)
    is_in_navbar = models.BooleanField()
    content = models.TextField()
    
    def __unicode__(self):
        return self.nav_name

class Participant(models.Model):
  display_name = models.CharField(max_length=200)
  matric = models.CharField(max_length=8)
  is_leader = models.BooleanField(default=False)
  team = models.ForeignKey('Team', null=True, related_name='members')
  user = models.OneToOneField(User)


class Team(models.Model):
  name = models.CharField(max_length=200, unique=True)
  project = models.OneToOneField('Project', null=True, related_name='leaderof')


class Project(models.Model):
  name = models.CharField(max_length=200, unique=True)
  pitch = models.TextField(blank=True)
  web = models.URLField(null=True, blank=True)
  repo = models.URLField(null=True, blank=True)