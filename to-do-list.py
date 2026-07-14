import json

filename = "todo_list.json"

def load_tasks():
    try:
        with open(filename , "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}
    
def save_tasks(tasks):
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file)
    except:
        print("Error saving tasks to file.")

def add_tasks():
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
    print('''1. Add tasks
2. Mark Tasks as Complete
3. Delete Tasks
4. Display Tasks
5. Save tasks
6. Exit''')
    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            print("Add tasks")
            add_tasks()
        elif choice == '2':
            print("Mark tasks as complete")
            mark_tasks_complete()
        elif choice == '3':
            print("Delete tasks")
            delete_tasks()
        elif choice == '4':
            print("Display tasks")
            display_tasks()
        elif choice == '5':
            print("Save tasks")
            save_tasks(tasks)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()