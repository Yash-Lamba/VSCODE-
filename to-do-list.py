from asyncio import tasks
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

def add_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Description not given.") 

def display_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks present.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(task_list):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{idx + 1}. {task['description']} - {status}")
    
def delete_tasks(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete:"))
        if 1<= task_number <= len(tasks):
            del tasks["tasks"][task_number - 1]
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")


def mark_tasks_complete(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

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
            add_tasks(tasks)
        elif choice == '2':
            print("Mark tasks as complete")
            mark_tasks_complete(tasks)
        elif choice == '3':
            print("Delete tasks")
            delete_tasks(tasks)
        elif choice == '4':
            print()
            display_tasks(tasks)
        elif choice == '5':
            print("Save tasks")
            save_tasks(tasks)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()