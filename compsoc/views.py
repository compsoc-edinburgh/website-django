from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from compsoc.models import Page, Event

class PageView(TemplateView):
    template_name = 'compsoc/page.html'
    
    def get(self, request, page_name):
        context = { 'page': get_object_or_404(Page, name=page_name) }
        context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
        context['events'] = Event.objects.order_by('when').values()
        return render(request, self.template_name,  context)
    

