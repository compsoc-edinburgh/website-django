from django.contrib import admin
from ilwhack import models

admin.site.register(models.Page)
admin.site.register(models.Participant)
admin.site.register(models.Team)
admin.site.register(models.Project)
admin.site.register(models.ProjectPhoto)