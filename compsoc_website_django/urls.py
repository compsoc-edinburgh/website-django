from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from compsoc_website_django.views import HTTP404View, HTTP500View
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

# Error pages on development server
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404/$', HTTP404View.as_view()),
        url(r'^500/$', HTTP500View.as_view()),
    )

# File uploads on development server
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns