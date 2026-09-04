from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("create/", views.job_create, name="job_create"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
    path("<int:job_id>/edit/", views.job_update, name="job_update"),
    path("<int:job_id>/delete/", views.job_delete, name="job_delete"),
    path("mine/", views.my_jobs, name="my_jobs"),
    path("<int:job_id>/apply/", views.job_apply, name="job_apply"),
]