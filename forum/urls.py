from . import views
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^forum/$', views.HomeView.as_view(), name='home_page'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.PostList.as_view(), name='topic'),
    url(r'^$', views.LoginView.as_view(), name='login'),

]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]