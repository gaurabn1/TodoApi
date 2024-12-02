from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_remainder_mail


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Todo(models.Model):

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    author = models.ForeignKey(CustomUser, models.CASCADE, related_name="todos")
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='not_started', max_length=20) 
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, default='low', choices=PRIORITY_CHOICES)
    remainder_date = models.DateTimeField()

    def __str__(self):
        return self.title

@receiver(post_save, sender=Todo)
def send_email_on_remainder(sender, instance, created, **kwargs):
    if created and instance.due_date:
        subject = f"Reminder: {instance.title}"
        message = f"Hi {instance.author.username},\n\nDon't forget to complete your task '{instance.title}' by {instance.due_date}.\n\nBest regards,\nYour Todo App"
        recipient_email = instance.author.email
        send_remainder_mail.apply_async(
            args=[subject, message, recipient_email],
            eta = instance.due_date
        )
