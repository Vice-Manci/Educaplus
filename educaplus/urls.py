from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from . import views


app_name = "educaplus"
urlpatterns = [
    path("", views.logout, name="logout"),
    path("home", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
      path('tasks/', include("tasks.urls")),
]