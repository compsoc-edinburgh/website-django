from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from compsoc.models import Page, Event, Announcement
from compsoc.forms import SearchForm

import datetime


def get_base_context():
    context = {}
    context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
    context['announcements'] = Announcement.objects.filter(display__exact=True).values('content')
    context['events'] = Event.objects.order_by('when').filter(when__gt=datetime.datetime.now()).values()
    return context


class PageView(TemplateView):
    template_name = 'compsoc/page.html'

    def get(self, request, page_name):
        context = get_base_context()
        context['page'] = get_object_or_404(Page, name=page_name)
        context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
        context['events'] = Event.objects.filter(when__gte=datetime.date.today()).order_by('when').values()

        return render(request, self.template_name, context)


class SearchView(TemplateView):
    template_name = 'compsoc/search.html'

    def get(self, request):
        form = SearchForm(request.GET)

        if form.is_valid():

            query = form.cleaned_data['query']
            context = get_base_context()
            # TODO make this more efficient maybe
            context['page_results'] = Page.objects.filter(content__icontains=query).values('name', 'title') or []
            # TODO something here, ask R2ZER0
            # context.event_results = Event.objects.filter(description__icontains=query).values('url', 'title')
            context['query'] = query
            return render(request, self.template_name, context)

        else:
            return render(request, self.template_name, {})


class IrcView(TemplateView):
    template_name = 'compsoc/irc.html'

    def get(self, request):
        return render(request, self.template_name, {})
