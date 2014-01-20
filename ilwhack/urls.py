from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from ilwhack import views

urlpatterns = patterns('', 
    url('^$', views.HomeView.as_view(), name='home')
)
  
