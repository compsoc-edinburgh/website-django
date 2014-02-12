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
    real_name = models.CharField(max_length=200, blank=True, null=True)
    matric_no = models.CharField(max_length=8)
    department = models.CharField(max_length=100, help_text='E.g. Informatics, Business, Design, etc')
    bio = models.TextField()
    is_leader = models.BooleanField(default=False)
    team = models.ForeignKey('Team', null=True, related_name='members')
    user = models.OneToOneField(User)
    
    def leave_team(self):
        theteam = self.team
        self.is_leader = False
        self.team = None
        self.save()
        if not theteam.members.exists():
            if theteam.project:
                theteam.project.delete()
            theteam.delete()
        else:
            newleader = theteam.members.all()[0]
            newleader.is_leader = True
            newleader.save()
    
    def give_leader_to(self, who):
        if self.is_leader and self.team == who.team:
            who.is_leader = True
            who.save()
            self.is_leader = False
            self.save()
  
    def __unicode__(self):
        return self.display_name


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    project = models.OneToOneField('Project', null=True, blank=True)
    
    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    pitch = models.TextField(blank=True)
    web = models.URLField(null=True, blank=True)
    repo = models.URLField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class ProjectPhoto(models.Model):
    caption = models.TextField(blank=True, null=True)
    file = models.ImageField(upload_to='project-photos/')
    project = models.ForeignKey(Project, related_name='photos')
    
    def __unicode__(self):
        if self.caption:
            return '' + self.project.name + ': ' + self.caption[0:20]
        else:
            return '' + self.project.name + ': Photo ID#' + str(self.id)
    