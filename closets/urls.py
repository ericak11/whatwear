from django.conf.urls import patterns, url
from closets import views
from closets.views import OwnerList, ClosetList, ClosetCreate, ClosetUpdate, ClosetDelete, OwnerCreate
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
      url(r'^$', login_required(OwnerList.as_view())),
      url(r'owners/add/$', OwnerCreate.as_view(), name='owner_add'),
      url(r'closets/add/$', ClosetCreate.as_view(), name='closet_add'),
      url(r'^closets/([\w-]+)/$', ClosetList.as_view(), name='closet_list'),
      url(r'closets/(?P<pk>\d+)/update/$', ClosetUpdate.as_view(), name='closet_update'),
      url(r'closets/(?P<pk>\d+)/delete/$', ClosetDelete.as_view(), name='closet_delete'),
)
