from django.conf.urls import patterns, url
from closets import views
from closets.views import OwnerList, ClosetList

urlpatterns = patterns('',
      # url(r'^$', views.user_login, name='user_login'),
      url(r'^$', OwnerList.as_view()),
      url(r'^closets/([\w-]+)/$', ClosetList.as_view()),
)
