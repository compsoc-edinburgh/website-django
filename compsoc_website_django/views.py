from django.views.generic.base import TemplateView


class HTTP404View(TemplateView):
    template_name = '404.html'


class HTTP500View(TemplateView):
    template_name = '500.html'
