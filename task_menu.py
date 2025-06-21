from task import Task
from global_state import tasks
from db import add_task_to_db, get_all_tasks,update_task_status,delete_task_by_id

def add_task():
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    task_due_date = input("When is task due?: ")
    task_due_time = input("What time is task due(HH:MM in 24hr format): ")
    task_priority = input("Enter task priority (Low, Medium, High): ").capitalize()
    priority_value = Task.REVERSE_PRIORITY_MAP.get(task_priority, 2)
    task = Task(
        title=task_title,
        description=task_description, 
        priority=priority_value, 
        due_date=task_due_date,
        due_time=task_due_time
        )
    add_task_to_db(task)
    print("Task Added")

def view_task():
    print("\nView Tasks")
    sort_by = input("Sort by (priority / due_date / title)? [priority]: ").strip() or "priority"
    filter_status = input("Filter by status? (all / completed / pending) [all]: ").strip().lower()
    
    completed_filter = None
    if filter_status == 'completed':
        completed_filter = True
    elif filter_status == 'pending':
        completed_filter = False
        
    tasks = get_all_tasks(sort_by=sort_by, completed_filter=completed_filter)
    
    if not tasks:
        print('No task found.')
        
    for task in tasks:
        print(task)

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
    