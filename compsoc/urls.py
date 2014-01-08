from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from compsoc import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/compsoc/home'), name='go-to-home'),
    url(r'^(?P<page_name>\w+)', views.PageView.as_view(), name='page'),
)