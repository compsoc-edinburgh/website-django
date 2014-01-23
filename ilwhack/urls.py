from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from ilwhack import views

urlpatterns = patterns('', 
    url(r'^$', RedirectView.as_view(url='/ilwhack/page/home'), name='ilw-go-to-home'),
    url(r'^page/(?P<page_name>[\w\-_]+)', views.PageView.as_view(), name='ilw-page'),
)
  
