from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView, TemplateView
from compsoc_website_django.views import HTTP404View
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compsoc_website_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url="/compsoc/page/home"), name="go-to-home"),
    url(r'^compsoc/', include('compsoc.urls')),
    url(r'^ilwhack/', include('ilwhack.urls')),
    url(r'^ledger/',  include('ledger.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404/$', HTTP404View.as_view()),
    )