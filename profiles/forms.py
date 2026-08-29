from django import forms
from .models import CandidateProfile, CompanyProfile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = [
            "bio",
            "skills",
            "experience",
            "education",
            "location",
            "phone_number",
            "linkedin_url",
            "profile_image",
            "resume",
        ]


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [
            "company_name",
            "website",
            "description",
            "industry",
            "company_size",
            "location",
            "profile_image",
        ]
