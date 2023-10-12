from ..tasks import send_email_with_retry
# 当任务到期或任务被分配时，出发邮件发送
def check_task_conditions(task):
    if task.is_about_to_expire():
        send_email_with_retry.apply_async(('1290a45s@gmail.com', 'You task is about to expire'), countdown=5)
    elif task.is_newly_assigned():
        send_email_with_retry.apply_async(('1290a45s@gmail.com', 'You have a new task'), countdown=5)