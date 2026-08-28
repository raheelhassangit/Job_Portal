from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    class Role(models.TextChoices):
        CANDIDATE = "candidate", "Candidate"
        COMPANY = "company", "Company"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        blank = True
    )
    
    REQUIRED_FIELDS = ["email"]