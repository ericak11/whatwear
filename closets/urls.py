from django.conf.urls import patterns, url
from closets import views
from closets.views import UserList, ClosetList, ClosetCreate, ClosetUpdate, ClosetDelete
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
      url(r'^$', login_required(UserList.as_view())),
      url(r'closets/add/$', ClosetCreate.as_view(), name='closet_add'),
      url(r'^closets/([\w-]+)/$', ClosetList.as_view(), name='closet_list'),
      url(r'closets/(?P<pk>\d+)/update/$', ClosetUpdate.as_view(), name='closet_update'),
      url(r'closets/(?P<pk>\d+)/delete/$', ClosetDelete.as_view(), name='closet_delete'),
)
