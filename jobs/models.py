from django.db import models
from django.conf import settings
from profiles.models import CompanyProfile


class Job(models.Model):
    class JobType(models.TextChoices):
        FULL_TIME = "full_time", "Full-time"
        PART_TIME = "part_time", "Part-time"
        CONTRACT = "contract", "Contract"
        REMOTE = "remote", "Remote"

    class ExperienceLevel(models.TextChoices):
        ENTRY = "entry", "Entry Level"
        MID = "mid", "Mid Level"
        SENIOR = "senior", "Senior Level"

    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    experience_level = models.CharField(max_length=20, choices=ExperienceLevel.choices)
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company.company_name}"