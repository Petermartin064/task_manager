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
                description TEXT,
                due_date TEXT,
                due_time TEXT,
                priority INTEGER,
                completed INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def add_task_to_db(task: Task):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO tasks (title, description, due_date, due_time, priority, completed)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task.title, task.description, task.due_date, task.due_time, task.priority, int(task.completed)))
        conn.commit()

def get_all_tasks(sort_by='priority', completed_filter=None):
    query = '''
        SELECT id, title, description, due_date, due_time, priority, completed
        FROM tasks
    '''
    params = []

    if completed_filter is not None:
        query += ' WHERE completed = ?'
        params.append(int(completed_filter))

    query += f' ORDER BY {sort_by} ASC'

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(query, params)
        rows = c.fetchall()
        return [
            Task(id=row[0], title=row[1], description=row[2], due_date=row[3], due_time=row[4],
                priority=row[5], completed=bool(row[6]))
            for row in rows
        ]

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

def update_task_in_db(task):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?, due_time = ?, priority = ?, completed = ?
            WHERE id = ?
        ''', (task.title, task.description, task.due_date, task.due_time, task.priority, int(task.completed), task.id))
        conn.commit()
