# A to do list
# load existing tasks from a file 
# check if they are complete or not(mark them as complete or incomplete)
# add new tasks 
# delete tasks

def load_tasks():
    pass

def add_and_save_tasks():
    pass

def mark_tasks_complete():
    pass   

def delete_tasks():
    pass

def display_tasks():
    pass

def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List!")
    print('''1. Add and save Tasks
2. Mark Tasks as Complete
3. Delete Tasks
4. Display Tasks
5. Exit''')
    
    while True:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            print("Add and save tasks")
            add_and_save_tasks()
        elif choice == 2:
            print("Mark tasks as complete")
            mark_tasks_complete()
        elif choice == 3:
            print("Delete tasks")
            delete_tasks()
        elif choice == 4:
            print("Display tasks")
            display_tasks()
        elif choice == 5:
            print("Exiting the To-Do List. Goodbye!")
            break