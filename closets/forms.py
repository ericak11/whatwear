from django.contrib.auth.models import User
from closets.models import Owner, Closet, Item, Tag
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='Email', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'gender')


class ClosetForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ('name', 'location',)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'content', 'category', 'photo', 'tags',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ('name',)

