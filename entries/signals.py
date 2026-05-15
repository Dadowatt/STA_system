from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entry


@receiver(post_save, sender=Entry)
def log_entry_creation(sender, instance, created, **kwargs):
    if created:
        print(f"[LOG] Entry créée par {instance.auteur.username} le {instance.date_creation}")