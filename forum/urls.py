from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home_page'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.PostList.as_view(), name='topic'),
    # url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^post/edit/.*$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),

]
