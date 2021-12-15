from django.forms.forms import Form
from django.shortcuts import redirect, render
from django import forms
from django.urls.base import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def logout(request):
      return render(request, "educaplus/logout.html")

def registro(request):
      data = {
            'form': CustomUserCreationForm()
      }

      if request.method == 'POST':
            formulario = CustomUserCreationForm(data=request.POST)
            if formulario.is_valid():
                  formulario.save()
                  user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                  login(request, user)
                  messages.success(request, "Te has registrado correctamente.")
                  return redirect(to="login")
            data["form"] = formulario

      return render(request, "registration/registro.html", data)

@login_required
def index(request):
      return render(request, "educaplus/index.html")


