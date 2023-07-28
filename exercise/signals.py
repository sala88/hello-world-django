from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        print("E' stato creato un nuovo studente:", instance.first_name, instance.last_name)