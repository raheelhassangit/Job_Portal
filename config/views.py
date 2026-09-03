from django.shortcuts import render
from jobs.models import Job


def home(request):
    recent_jobs = Job.objects.filter(is_active=True).order_by("-posted_at")[:4]
    return render(request, "home.html", {"recent_jobs": recent_jobs})