from django.db import models


class Ledger(models.Model):
    date = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.date.strftime('%d/%m/%Y at %H:%M')
