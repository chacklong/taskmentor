
from celery import shared_task
from .models.send_email import send_advanced_email

@shared_task(bind=True, max_retries=3)
def send_email_with_retry(self, user_email, task_name):
    try:
        send_advanced_email(user_email, task_name)
    except Exception as exc:
        raise self.retry(exc=exc)