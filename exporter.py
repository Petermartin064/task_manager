import csv
import json

from task import Task
from task_menu import get_all_tasks

def export_tasks(format='csv', file_name='task_export'):
    """Return export types options"""
    tasks = get_all_tasks()
    if not tasks:
        print("No task to export")
        return
    
    if format == 'csv':
        export_to_csv(tasks, f"{file_name}.csv")
    
    elif format == 'json':
        export_to_json(tasks, f"{file_name}.json")
    
    elif format == 'txt':
        export_to_txt(tasks, f"{file_name}.txt")

def export_to_csv(tasks, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'Due Date', 'Due Time', 'Priority', 'Status', 'Description'])
        for t in tasks:
            writer.writerow([
                t.id, t.title, t.due_date, t.due_time,
                Task.PRIORITY_MAP.get(t.priority, 'Unknown'),
                'Completed' if t.completed else 'Pending',
                t.description
            ])
    print(f"Tasks exported to {file_name} ✅")

def export_to_json(tasks, file_name):
    with open(file_name, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)
    print(f"Tasks exported to {file_name} ✅")

def export_to_txt(tasks, file_name):
    with open(file_name, 'w') as f:
        for t in tasks:
            f.write(t.to_plaintext() + '\n' + '-'*40 + '\n')
        print(f"Tasks exported to {file_name} ✅")