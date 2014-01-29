from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

class RegisterView(TemplateView):
    template_name = "accounts/register.html"
    
