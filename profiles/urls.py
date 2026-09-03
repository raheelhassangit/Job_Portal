from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("setup/", views.profile_setup, name="profile_setup"),
    path("me/", views.profile_view, name="profile_view"),
    path("candidates/", views.find_candidates, name="find_candidates"),
    path("companies/", views.browse_companies, name="browse_companies"),
]