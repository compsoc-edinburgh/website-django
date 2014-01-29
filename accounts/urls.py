from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^register/', views.RegisterView.as_view()),
)