from task import Task
from global_state import tasks
from db import add_task_to_db, get_all_tasks,update_task_status,delete_task_by_id, update_task_in_db

def add_task():
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    task_due_date = input("When is task due?((YYYY-MM-DD)): ")
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

def edit_task():
    tasks = get_all_tasks(sort_by='id')
    
    if not tasks:
        print("No available task to edit.")
        return
        
    for task in tasks:
        print(task)
    
    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("Enter a valid ID")
        return
    
    task_to_edit = next((t for t in tasks if t.id == task_id), None)
    
    if not task_to_edit:
        print("Task Not Found")
        return
    
    print("\nPress enter to keep the current values")
    
    title = input(f"Title [{task_to_edit.title}]: ") or task_to_edit.title
    description = input(f"Description [{task_to_edit.description}]: ") or task_to_edit.description
    due_date = input(f"Due Date (YYYY-MM-DD) [{task_to_edit.due_date}]: ") or task_to_edit.due_date
    due_time = input(f"Due Time (HH:MM) [{task_to_edit.due_time}]: ") or task_to_edit.due_time
    
    priority_label = Task.PRIORITY_MAP.get(task_to_edit.priority, 'Medium')
    priority_input = input(f"Priority (Low/Medium/High) [{priority_label}]: ")
    if priority_input:
        priority = Task.REVERSE_PRIORITY_MAP.get(priority_input.capitalize(), task_to_edit.priority)
    else:
        priority = task_to_edit.priority
        
    completed_input = input(f"Completed? (yes/no) [{ 'yes' if task_to_edit.completed else 'no' }]: ")
    if completed_input.lower() in ['yes', 'y']:
        completed = True
    elif completed_input.lower() in ['no', 'n']:
        completed = False
    else:
        completed = task_to_edit.completed
        
    task_to_edit.title = title
    task_to_edit.description = description
    task_to_edit.due_date = due_date
    task_to_edit.due_time = due_time
    task_to_edit.priority = priority
    task_to_edit.completed = completed
    
    update_task_in_db(task_to_edit)
    print("✅ Task updated successfully.")