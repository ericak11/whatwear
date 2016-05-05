from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from closets.models import Closet, Tag, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ClosetCreate(CreateView):
    model = Closet
    fields = ['name', 'location']
    template_name = 'closet/new.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClosetCreate, self).form_valid(form)

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
        self.user = get_object_or_404(User, id=self.args[0])
        return Closet.objects.filter(user=self.user)

class UserList(ListView):
    model = User
    template_name = 'user/list.html'

class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'content', 'category', 'photo', 'tags']
    template_name = 'item/new.html'
    def form_valid(self, form, **kwargs):
        self.closet = get_object_or_404(Closet, id=self.kwargs.get("closetid"))
        form.instance.closet = self.closet
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(UpdateView):
    model = Item
    template_name = 'item/new.html'

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')

class ItemList(ListView):
    template_name = 'item/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.closet = get_object_or_404(Closet, id=self.args[0])
        context = super(ItemList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['item_list'] = Item.objects.filter(closet=self.closet)
        context['closet'] =  self.closet
        return context
    def get_queryset(self):
        self.closet = get_object_or_404(Closet, id=self.args[0])
        return Item.objects.filter(closet=self.closet)

class TagCreate(CreateView):
    model = Tag
    template_name = 'tag/new.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'
