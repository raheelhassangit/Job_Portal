from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .forms import CandidateProfileForm, CompanyProfileForm


@login_required
def profile_setup(request):
    if request.user.role == User.Role.CANDIDATE:
        profile = request.user.candidate_profile
        form_class = CandidateProfileForm
    else:
        profile = request.user.company_profile
        form_class = CompanyProfileForm

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile_setup")
    else:
        form = form_class(instance=profile)

    return render(request, "profiles/profile_setup.html", {"form": form})