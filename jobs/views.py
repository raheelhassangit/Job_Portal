from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from .models import Job
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required
def job_create(request):
    if request.user.role != "company":
        raise PermissionDenied("Only companies can create jobs.")

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company_profile
            job.save()
            return redirect("jobs:job_detail", job_id=job.pk)
    else:
        form = JobForm()

    return render(request, "jobs/job_create.html", {"form": form})


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    return render(request, "jobs/job_detail.html", {"job": job})


@login_required
def job_update(request, job_id):
    if request.user.role != "company":
        raise PermissionDenied("Only companies can update jobs.")

    job = get_object_or_404(Job, pk=job_id, company=request.user.company_profile)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("jobs:job_detail", job_id=job.pk)
    else:
        form = JobForm(instance=job)

    return render(request, "jobs/job_update.html", {"form": form, "job": job})


@login_required
def job_delete(request, job_id):
    if request.user.role != "company":
        raise PermissionDenied("Only companies can delete jobs.")

    job = get_object_or_404(Job, pk=job_id, company=request.user.company_profile)

    if request.method == "POST":
        job.is_active = False
        job.save()
        return redirect("jobs:job_list")

    return render(request, "jobs/job_delete.html", {"job": job})

@login_required
def my_jobs(request):
    if request.user.role != "company":
        raise PermissionDenied("Only companies can view their job postings.")

    jobs = Job.objects.filter(company=request.user.company_profile).order_by("-posted_at")
    return render(request, "jobs/my_jobs.html", {"jobs": jobs})