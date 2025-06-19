from task import Task
from global_state import tasks

def add_task():
    task_title = input("Enter the tasks title: ")
    task_due_date = input("Enter task's due date: ")
    task_priority = input("Enter task priority (low, medium, high): ")
    task = Task(title=task_title, priority=task_priority, due_date=task_due_date)
    tasks.append(task)
    print("Task Added")

def view_task():
    if not tasks:
        print("No task added yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def change_task_status():
    view_task()
    try:
        choice = int(input('Enter task number to mark as completed: ')) -1
        tasks[choice].completed = True
        print('Status changed successfully')
    except (IndexError, ValueError):
        print('Invalid task value')

def delete_task():
    view_task()
    choice = int(input("Enter a task number you want deleted: ")) -1
    deleted = tasks.pop(choice)
    print(f"{deleted.title} is deleted successfully")
    