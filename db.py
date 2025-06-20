import sqlite3
from task import Task

DB_NAME = 'tasks.db'

def init_db():
    """Create tasks table if it doesn't exist"""
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                due_date TEXT,
                priority TEXT,
                completed INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def add_task_to_db(task: Task):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO tasks (title, due_date, priority, completed)
            VALUES (?, ?, ?, ?)
        ''', (task.title, task.due_date, task.priority, int(task.completed)))
        conn.commit()

def get_all_tasks(sort_by='priority'):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(f'''
            SELECT id, title, due_date, priority, completed
            FROM tasks
            ORDER BY {sort_by} ASC
        ''')
        rows = c.fetchall()
        return [Task(id=row[0], title=row[1], due_date=row[2], priority=row[3], completed=bool(row[4])) for row in rows]

def update_task_status(task_id: int, completed: bool):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('UPDATE tasks SET completed = ? WHERE id = ?', (int(completed), task_id))
        conn.commit()

def delete_task_by_id(task_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
