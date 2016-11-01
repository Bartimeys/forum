from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^home$', views.HomeView.as_view(), name='home_page'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.PostList.as_view(), name='topic'),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='post_update_form'),
    url(r'^$', views.Register.as_view(), name='accounts-register'),
    url(r'login/', views.Login.as_view(), name='accounts-login'),
    url(r'logout/$', views.Logout.as_view(), name='accounts-logout'),
    url(r'success/', login_required(views.Success.as_view(), login_url='/accounts-login'), name='accounts-success'),

]
