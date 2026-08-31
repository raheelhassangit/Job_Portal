from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .forms import CandidateProfileForm, CompanyProfileForm


@login_required
def profile_setup(request):
    if request.user.role == User.Role.CANDIDATE:
        profile = request.user.candidate_profile
        form_class = CandidateProfileForm
        template_name = "profiles/candidate_profile_setup.html"
    else:
        profile = request.user.company_profile
        form_class = CompanyProfileForm
        template_name = "profiles/company_profile_setup.html"

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile_view")
    else:
        form = form_class(instance=profile)

    return render(request, template_name, {"form": form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_view(request):
    if request.user.role == "candidate":
        return render(
            request,
            "profiles/candidate_profile_view.html",
            {"profile": request.user.candidate_profile},
        )
    else:
        return render(
            request,
            "profiles/company_profile_view.html",
            {"profile": request.user.company_profile},
        )