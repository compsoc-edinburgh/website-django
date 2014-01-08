from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from compsoc import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/compsoc/page/home'), name='go-to-home'),
    url(r'^page/(?P<page_name>\w+)', views.PageView.as_view(), name='page'),
    url(r'^search', views.SearchView.as_view(), name='search'),
)