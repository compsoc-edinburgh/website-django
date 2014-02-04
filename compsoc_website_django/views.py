from django.views.generic.base import RedirectView, TemplateView 

class HTTP404View(TemplateView):
    template_name = '404.html'
