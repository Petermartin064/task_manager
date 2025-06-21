import os

from colorama import Fore, Style, init

from task_menu import add_task, view_task, change_task_status, delete_task, edit_task, send_due_task_reminders
from save_and_load_task import load_tasks, save_tasks
from db import init_db

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(Fore.CYAN + Style.BRIGHT + "\n📋 Task Manager")
    print(Fore.YELLOW + "1." + Style.RESET_ALL + " Add Task")
    print(Fore.YELLOW + "2." + Style.RESET_ALL + " View Tasks")
    print(Fore.YELLOW + "3." + Style.RESET_ALL + " Change Task Status")
    print(Fore.YELLOW + "4." + Style.RESET_ALL + " Delete Task")
    print(Fore.YELLOW + "5." + Style.RESET_ALL + " Edit Task")
    print(Fore.YELLOW + "6." + Style.RESET_ALL + " Exit\n")
    
def main():
    
    try:
        init_db()
        load_tasks()
        send_due_task_reminders()
        while True:
            menu()
            choice = input('Choose an option: ')
            if choice == '1':
                clear()
                add_task()
                
            elif choice == '2':
                view_task()
                
            elif choice == '3':
                change_task_status()
                
            elif choice == '4':
                delete_task()
            
            elif choice == '5':
                edit_task()
                
            elif choice == '6':
                save_tasks()
                print("Exiting Task Manager")
                break
    except KeyboardInterrupt:
        save_tasks()
        print("\nExiting Task Manager")

if __name__ == '__main__':
    main()