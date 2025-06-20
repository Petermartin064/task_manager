from task import Task
from global_state import tasks
from db import add_task_to_db, get_all_tasks,update_task_status,delete_task_by_id

def add_task():
    task_title = input("Enter the tasks title: ")
    task_due_date = input("Enter task's due date: ")
    task_priority = input("Enter task priority (low, medium, high): ")
    task = Task(title=task_title, priority=task_priority, due_date=task_due_date)
    add_task_to_db(task)
    print("Task Added")

def view_task():
    tasks = get_all_tasks()
    if not tasks:
        print("No task added yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{task}")

def change_task_status():
    view_task()
    task_id = int(input("Enter task ID to mark as completed: "))
    update_task_status(task_id, completed=True)
    print("Task marked as completed.")


def delete_task():
    view_task()
    task_id = int(input("Enter task ID to delete: "))
    delete_task_by_id(task_id)
    print("Task deleted.")
    