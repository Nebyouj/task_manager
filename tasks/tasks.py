from celery import shared_task
from .models import Task
from django.conf import settings

@shared_task
def send_task_email(task_id):
    from django.core.mail import send_mail
    try:
        task = Task.objects.get(id=task_id)
        subject = f"Task Created: {task.title}"
        message = f"Task Details:\n\nTitle: {task.title}\nDescription: {task.description}\nCompleted: {task.completed}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
    except Task.DoesNotExist:
        pass