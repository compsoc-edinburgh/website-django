from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from ilwhack.models import Page

class PageView(TemplateView):
    template_name = 'ilwhack/page.html'
    
    def get(self, request, page_name):
        context = { 'page': get_object_or_404(Page, name = page_name) }
        context['nav_pages'] = Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')
        return render(request, self.template_name,  context)


class RegisterView(TemplateView):
    template_name = 'ilwhack/register.html'
    
    def get(self, request):
        return render(request, self.template_name, { 'form': UserCreationForm() })
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data.get('username'), None, form.cleaned_data.get('password'))
            return HttpResponseRedirect('/ilwhack/')
        
        else:
           return render(request, self.template_name, { 'form': form })