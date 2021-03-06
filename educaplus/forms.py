from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

      username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
      email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

      class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']