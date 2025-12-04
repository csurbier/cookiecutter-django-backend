"""
Celery tasks for users app.
"""
{% if cookiecutter.use_celery == "yes" %}
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_email, user_name):
    """
    Send a welcome email to a new user.
    
    Args:
        user_email: Email address of the user
        user_name: Name of the user
    """
    subject = 'Bienvenue sur {{ cookiecutter.project_name }}'
    message = f'Bonjour {user_name},\n\nBienvenue sur {{ cookiecutter.project_name }}!'
    from_email = settings.DEFAULT_FROM_EMAIL
    
    send_mail(
        subject,
        message,
        from_email,
        [user_email],
        fail_silently=False,
    )
    return f'Welcome email sent to {user_email}'
{% endif %}

