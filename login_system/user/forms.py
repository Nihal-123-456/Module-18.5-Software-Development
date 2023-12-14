from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.forms import *

class signup(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class editprofile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']