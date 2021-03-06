from django.contrib import admin
from compsoc.models import Page, Event, Announcement


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Page Meta', {'fields': ['name', 'nav_name', 'is_in_navbar', 'content_markup']}),
        ('Page Content', {'fields': ['title', 'content']})
    ]

admin.site.register(Page, PageAdmin)
admin.site.register(Event)
admin.site.register(Announcement)
