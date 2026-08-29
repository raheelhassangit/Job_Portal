from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from profiles.models import CandidateProfile, CompanyProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.CANDIDATE:
            CandidateProfile.objects.create(user=instance)
        elif instance.role == User.Role.COMPANY:
            CompanyProfile.objects.create(user=instance)