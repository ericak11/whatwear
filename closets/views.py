from django.shortcuts import render
from django.views.generic import ListView
from closets.models import Owner, Closet, Tag, Item
# Create your views here.

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/list.html'
