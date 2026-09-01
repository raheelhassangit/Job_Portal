from django.contrib import admin
from .models import CandidateProfile, CompanyProfile

# Register your models here.

admin.site.register(CompanyProfile)
admin.site.register(CandidateProfile)