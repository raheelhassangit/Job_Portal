from django.db import models
from accounts.models import User


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=500, blank=True, help_text="Comma-separated, e.g. Python, Django, SQL")
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to="candidate_images/", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class CompanyProfile(models.Model):
    COMPANY_SIZE_CHOICES = [
        ("1-10", "1-10 employees"),
        ("11-50", "11-50 employees"),
        ("51-200", "51-200 employees"),
        ("201-500", "201-500 employees"),
        ("500+", "500+ employees"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company_profile")
    company_name = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    company_size = models.CharField(max_length=20, choices=COMPANY_SIZE_CHOICES, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="company_logos/", blank=True, null=True)

    def __str__(self):
        return self.company_name or self.user.username