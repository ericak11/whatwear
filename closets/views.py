from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from closets.models import Owner, Closet, Tag, Item
# Create your views here.

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/list.html'

class ClosetList(ListView):
    template_name = 'closet/list.html'
    def get_queryset(self):
        self.owner = get_object_or_404(Owner, id=self.args[0])
        return Closet.objects.filter(owner=self.owner)
