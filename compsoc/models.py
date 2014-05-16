from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=128)
    nav_name = models.CharField(max_length=128)
    is_in_navbar = models.BooleanField()
    content_markup = models.CharField(max_length=128, choices=[('markdown', 'Markdown'), ('plain', 'Plain Text'),
                                                               ('html', 'HTML')])
    title = models.CharField(max_length=128)
    content = models.TextField()
    
    def __unicode__(self):
        return self.title


class Event(models.Model):
    when = models.DateTimeField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    is_in_gallery = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title


class Announcement(models.Model):
    content = models.TextField()
    display = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.content
