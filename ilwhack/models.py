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
  user = models.ForeignKey(User)
  is_leader = models.BooleanField(default=False)
  team = models.ForeignKey('Team', null=True, blank=True, related_name='members')
  
  def __unicode__(self):
      return self.user.username


class Team(models.Model):
  name = models.CharField(max_length=200, unique=True)
  project = models.OneToOneField('Project', null=True, related_name='leaderof')
  
  def __unicode__(self):
      return self.name


class Project(models.Model):
  name = models.CharField(max_length=200, unique=True)
  pitch = models.TextField(blank=True)
  web = models.URLField(null=True, blank=True)
  repo = models.URLField(null=True, blank=True)
  
  def __unicode__(self):
        self.name