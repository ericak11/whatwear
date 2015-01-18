from django.conf.urls import patterns, url
from closets import views
from closets.views import OwnerList

urlpatterns = patterns('',
      # url(r'^$', views.user_login, name='user_login'),
      url(r'^$', OwnerList.as_view()),
)
