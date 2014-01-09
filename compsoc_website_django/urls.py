from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from compsoc import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compsoc_website_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url="/compsoc/page/home"), name="go-to-home"),
    url(r'^compsoc/', include('compsoc.urls')),
    url(r'^ledger/', include('ledger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
