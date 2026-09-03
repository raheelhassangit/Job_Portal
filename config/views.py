from django.shortcuts import render
from jobs.models import Job
from profiles.models import CompanyProfile, CandidateProfile


def home(request):
    recent_jobs = Job.objects.filter(is_active=True).order_by("-posted_at")[:6]
    stats = {
        "jobs": Job.objects.filter(is_active=True).count(),
        "companies": CompanyProfile.objects.exclude(company_name="").count(),
        "candidates": CandidateProfile.objects.exclude(bio="").count(),
    }
    return render(request, "home.html", {"recent_jobs": recent_jobs, "stats": stats})