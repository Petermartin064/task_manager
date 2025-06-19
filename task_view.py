from task_menu import add_task, view_task, change_task_status, delete_task
from save_and_load_task import load_tasks, save_tasks

def menu():
    print('Task Manager\n')
    print('1. Add task')
    print('2. View Task')
    print('3. Change Task Status')
    print('4. Delete Task')
    print('5. Exit')
    
def main():
    menu()
    load_tasks()
    while True:
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
            print("Exiting Task Manager, Bye")
            break

if __name__ == '__main__':
    main()