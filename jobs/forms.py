from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "requirements",
            "location",
            "job_type",
            "experience_level",
            "salary_min",
            "salary_max",
        ]
        