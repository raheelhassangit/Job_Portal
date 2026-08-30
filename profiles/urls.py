from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("setup/", views.profile_setup, name="profile_setup"),
]