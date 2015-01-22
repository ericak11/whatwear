from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from closets.models import Owner, Closet, Tag, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ClosetCreate(CreateView):
    model = Closet
    fields = ['name', 'location']
    template_name = 'closet/new.html'

class ClosetUpdate(UpdateView):
    model = Closet
    fields = ['name', 'location']
    template_name = 'closet/new.html'

class ClosetDelete(DeleteView):
    model = Closet
    success_url = reverse_lazy('closet_list')

class ClosetList(ListView):
    template_name = 'closet/list.html'
    def get_queryset(self):
        self.owner = get_object_or_404(Owner, id=self.args[0])
        return Closet.objects.filter(owner=self.owner)

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/list.html'

class OwnerCreate(CreateView):
    model = User
    template_name = 'owner/new.html'
