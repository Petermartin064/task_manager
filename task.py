class Task:
    """Task definition"""
    PRIORITY_MAP = {1: "Low", 2: "Medium", 3: "High"}
    REVERSE_PRIORITY_MAP = {v: k for k, v in PRIORITY_MAP.items()}
    def __init__(self, title='', priority=2, due_date='', completed=False, id=None):
        self.id=id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
    
    def __str__(self):
        status = 'completed' if self.completed else 'pending'
        priority_label = self.PRIORITY_MAP.get(self.priority, "unknown")
            
        return f"{self.id}. {self.title} | Due: {self.due_date} | Priority: {priority_label} | Status: {status}"
    
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