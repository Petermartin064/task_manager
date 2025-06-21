from datetime import datetime

class Task:
    """Task definition"""
    PRIORITY_MAP = {1: "Low", 2: "Medium", 3: "High"}
    REVERSE_PRIORITY_MAP = {v: k for k, v in PRIORITY_MAP.items()}
    
    def __init__(self, title, description, priority=2, due_date='', due_time='', completed=False, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.due_time = due_time
        self.completed = completed
        
    def is_overdue(self):
        if self.completed:
            return False
        
        if not self.due_date or not self.due_time:
            return False
        
        try:
            due_datetime = datetime.strptime(f"{self.due_date} {self.due_time}", "%Y-%m-%d %H:%M")
            return datetime.now() > due_datetime
        except ValueError:
            return False
    
    def __str__(self):
        from colorama import Fore, Style

        status = f"{Fore.GREEN}✅ Completed" if self.completed else f"{Fore.YELLOW}⏳ Pending"
        if self.is_overdue():
            status += f" {Fore.RED}⚠️ Overdue"

        priority_label = self.PRIORITY_MAP.get(self.priority, "Unknown")
        return (
            f"{Fore.CYAN}{self.id}. {Style.BRIGHT}{self.title}{Style.RESET_ALL} | "
            f"{Fore.MAGENTA}Due: {self.due_date} {self.due_time} | "
            f"Priority: {priority_label} | Status: {status}\n"
            f"{Fore.BLUE}   Description: {self.description}{Style.RESET_ALL}"
        )
    
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