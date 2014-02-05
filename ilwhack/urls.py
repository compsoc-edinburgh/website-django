from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from ilwhack import views

urlpatterns = patterns('', 
    url(r'^$', RedirectView.as_view(url='/ilwhack/page/home'), name='ilw-go-to-home'),
    url(r'^page/(?P<page_name>[\w\-_]+)', views.PageView.as_view(), name='ilw-page'),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^myprofile/', 'ilwhack.views.myprofile'),
    url(r'^myaccount/$', 'ilwhack.views.myaccount'),
    url(r'^teams/', 'ilwhack.views.teams'),
    
    url(r'^myteam/$', 'ilwhack.views.myteam'),
    url(r'^myteam/leave/', 'ilwhack.views.myteam_leave'),
    url(r'^myteam/join/(\d+)/', 'ilwhack.views.myteam_join'),
    url(r'^myteam/makeleader/(\d+)/', 'ilwhack.views.myteam_makeleader'),
    
    url(r'^login/', 'django.contrib.auth.views.login',
        { 'template_name': 'ilwhack/login.html'}, name='ilw-login'),
    
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('ilw-go-to-home')}, name='ilw-logout'),
    
    url(r'^myaccount/changepassword/', 'django.contrib.auth.views.password_change', 
        {'template_name': 'ilwhack/changepassword.html', 'post_change_redirect': '/ilwhack/myaccount'}),

)
  
