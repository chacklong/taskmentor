from django.core.mail import send_mail, EmailMultiAlternatives

def send_completion_email(user_email, task_name):
    subject = f"Task {task_name} Completed"
    message = f"Congratulations! You have completed the task {task_name}."
    from_email = '1290a45s@gmail.com'
    recipient_list = [user_email]

    send_mail(subject, message , from_email, recipient_list)

def send_advanced_email(user_email, task_name):
    subject = f"Task {task_name} Completed"
    text_content = f"Congratulations ! You have completed the task {task_name}."
    html_content = f"<p>Congratulations ! You have <strong>completed</strong>the task {task_name}</p>"

    msg = EmailMultiAlternatives(subject, text_content, '1290a45s@gmail.com',[user_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()