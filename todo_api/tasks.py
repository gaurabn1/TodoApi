from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_remainder_mail(subject, message, receipient_email):
    send_mail(
        subject, 
        message,
        'sg3541679@gmail.com',
        [receipient_email],
        fail_silently=False
    )

