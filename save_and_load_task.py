import json
import os

from task import Task
from global_state import tasks

TASK_FILE = "tasks.json"

def save_tasks():
    """Save tasks to a json file"""
    with open(TASK_FILE, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
    print("\nTasks Saved")

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return
    with open(TASK_FILE, 'r') as f:
        data = json.load(f)
    
    tasks.clear()
    for item in data:
        tasks.append(Task.from_dict(item))
    print("Tasks Loaded successfully")