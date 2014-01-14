from django.db import models

# Create your models here.

class Ledger(models.Model):
    date = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.content
