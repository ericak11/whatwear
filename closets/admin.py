from django.contrib import admin
from django.contrib.auth.models import User
from closets.models import Closet, Item, Tag


# Register your models here.


# Re-register UserAdmin
admin.site.register(Closet)
admin.site.register(Item)
admin.site.register(Tag)
