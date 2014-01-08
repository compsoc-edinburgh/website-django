from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=128)
    nav_name = models.CharField(max_length=128)
    is_in_navbar = models.BooleanField()
    content_markup = models.CharField(max_length=128, choices=[('markdown', 'Markdown'),('plain', 'Plain Text'), ('html', 'HTML')])
    title = models.CharField(max_length=128)
    content = models.TextField()
    
    def __unicode__(self):
        return self.name