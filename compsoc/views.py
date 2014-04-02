from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from compsoc.models import Page, Event
from compsoc.forms import SearchForm

from datetime import date


class PageView(TemplateView):
    template_name = 'compsoc/page.html'

    def get(self, request, page_name):
        context = {'page': get_object_or_404(Page, name=page_name)}
        context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
        context['events'] = Event.objects.filter(when__gte=date.today()).order_by('when').values()
        return render(request, self.template_name,  context)


class SearchView(TemplateView):
    template_name = 'compsoc/search.html'

    def get(self, request):
        form = SearchForm(request.GET)

        if form.is_valid():

            query = form.cleaned_data['query']
            context = {}
            # TODO make this more efficient maybe
            context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
            context['page_results'] = Page.objects.filter(content__icontains=query).values('name', 'title') or []
            #context.event_results = Event.objects.filter(description__icontains=query).values('url', 'title') # TODO
            context['query'] = query
            return render(request, self.template_name, context)

        else:
            return render(request, self.template_name, {})

class IrcView(TemplateView):
    template_name = 'compsoc/irc.html'

    def get(self, request):
        return render(request, self.template_name, {})
