from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compsoc_website_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ledger.views.home'),
    url(r'^show/(?P<ledger_id>\d+)/$', 'ledger.views.view_ledger'),
)
