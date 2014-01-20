from django.db import models

class Participant(models.Model):
  username = models.CharField(max_length=200, unique=True)
  real_name = models.CharField(max_length=200)
  matric = models.CharField(max_length=8)
  email = models.EmailField()
  is_leader = models.BooleanField(default=False)
  team = models.ForeignKey('Team', null=True, related_name='members')


class Team(models.Model):
  name = models.CharField(max_length=200, unique=True)
  project = models.OneToOneField('Project', null=True, related_name='leaderof')


class Project(models.Model):
  name = models.CharField(max_length=200, unique=True)
  pitch = models.TextField(blank=True)
  web = models.URLField(null=True, blank=True)
  repo = models.URLField(null=True, blank=True)