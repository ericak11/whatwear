from django.conf.urls import patterns, url
from closets import views

urlpatterns = patterns('',
      url(r'^$', views.user_login, name='user_login'),
)
