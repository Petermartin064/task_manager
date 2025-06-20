from task_menu import add_task, view_task, change_task_status, delete_task
from save_and_load_task import load_tasks, save_tasks
from db import init_db

def menu():
    print('Task Manager\n')
    print('1. Add task')
    print('2. View Task')
    print('3. Change Task Status')
    print('4. Delete Task')
    print('5. Exit')
    
def main():
    init_db()
    while True:
        menu()
        choice = input('Choose an option: ')
        if choice == '1':
            add_task()
            
        elif choice == '2':
            view_task()
            
        elif choice == '3':
            change_task_status()
            
        elif choice == '4':
            delete_task()
            
        elif choice == '5':
            save_tasks()
            print("Exiting Task Manager")
            break

if __name__ == '__main__':
    main()