from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/topic/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
    url(r'^$', views.base, name='base'),


]