from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    class Role(models.TextChoices):
        CANDIDATE = "candidate", "Candidate"
        COMPANY = "company", "Company"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
    )
    
    REQUIRED_FIELDS = ["email", "role"]