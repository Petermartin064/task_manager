class Task:
    """Task definition"""
    def __init__(self, title='', priority='Medium', due_date='', completed=False, id=None):
        self.id=id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
    
    def __str__(self):
        status = 'completed' if self.completed else 'pending'
            
        return f"{self.id}. {self.title} | Due: {self.due_date} | Priority: {self.priority} | Status: {status}"
    
    def to_dict(self):
        return {
            'title': self.title,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            priority=data['priority'],
            due_date=data['due_date'],
            completed=data['completed']
        )