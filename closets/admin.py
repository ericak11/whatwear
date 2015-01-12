from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from closets.models import Owner
from closets.models import Closet
from closets.models import Item
# Register your models here.

class OwnerInline(admin.StackedInline):
    model = Owner
    can_delete = False
    verbose_name_plural = 'owner'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (OwnerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Closet)
admin.site.register(Item)
