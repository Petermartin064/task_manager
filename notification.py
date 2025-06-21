import subprocess

def notify_due_task(task):
    """Send a Linux desktop notification using notify-send."""
    title = f"⏰ Task Due Soon: {task.title}"
    message = f"Due: {task.due_date} {task.due_time}\nPriority: {task.priority}"
    subprocess.run(['notify-send', title, message])
