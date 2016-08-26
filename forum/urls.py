from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home_page'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.PostList.as_view(), name='topic')
]