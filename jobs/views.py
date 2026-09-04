from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q


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

    query = request.GET.get("q")
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) | Q(company__company_name__icontains=query)
        )

    job_type = request.GET.get("job_type")
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    experience_level = request.GET.get("experience_level")
    if experience_level:
        jobs = jobs.filter(experience_level=experience_level)

    location = request.GET.get("location")
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, "jobs/job_list.html", {
    "jobs": jobs,
    "query": query or "",
    "job_type": job_type or "",
    "experience_level": experience_level or "",
    "location": location or "",
    "job_type_choices": Job.JobType.choices,
    "experience_choices": Job.ExperienceLevel.choices,
    })


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    user_application = None
    if request.user.is_authenticated and request.user.role == "candidate":
        user_application = Application.objects.filter(job=job, candidate=request.user.candidate_profile).first()
    return render(request, "jobs/job_detail.html", {"job": job, "user_application": user_application})

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

@login_required
def job_apply(request, job_id):
    if request.user.role != "candidate":
        raise PermissionDenied("Only candidates can apply to jobs.")

    job = get_object_or_404(Job, pk=job_id, is_active=True)
    candidate = request.user.candidate_profile

    already_applied = Application.objects.filter(job=job, candidate=candidate).exists()

    if request.method == "POST" and not already_applied:
        cover_message = request.POST.get("cover_message", "")
        Application.objects.create(job=job, candidate=candidate, cover_message=cover_message)
        return redirect("jobs:job_detail", job_id=job.pk)

    return redirect("jobs:job_detail", job_id=job.pk)

@login_required
def job_applicants(request, job_id):
    if request.user.role != "company":
        raise PermissionDenied("Only companies can view applicants.")

    job = get_object_or_404(Job, pk=job_id, company=request.user.company_profile)
    applications = job.applications.select_related("candidate__user").order_by("-applied_at")

    return render(request, "jobs/job_applicants.html", {"job": job, "applications": applications})

@login_required
def my_applications(request):
    if request.user.role != "candidate":
        raise PermissionDenied("Only candidates can view their applications.")

    applications = Application.objects.filter(candidate=request.user.candidate_profile).select_related("job__company").order_by("-applied_at")

    return render(request, "jobs/my_applications.html", {"applications": applications})

@login_required
def withdraw_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id, candidate=request.user.candidate_profile)

    if request.method == "POST":
        application.delete()

    return redirect("jobs:my_applications")