# TO do Application

tasks = []

def menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit\n")

def add_task():
    new_task = input("\nPlease enter the task title: ")
    tasks.append({"title": new_task, "status": "Incomplete"})
    print(f"Task '{new_task}' added successfully!")

def view_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nTasks:")
        for x, task in enumerate(tasks, start=1):
            print(f"{x}. {task['title']}: {task['status']}")

def task_complete():
    try:
        print("\nHere are your tasks:")
        for x, task in enumerate(tasks, start=1):
            print(f"{x}. {task['title']}: {task['status']}")
        
        task_number = int(input("\nEnter the task number to mark as complete: "))
        if task_number <= 0 or task_number > len(tasks):
            raise IndexError
        tasks[task_number -1]["status"] = "Complete"
        print(f"Task{task_number} marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number. Please enter a valid number.")

def delete_task():
    try:
        print("\nHere are your tasks:")
        for x, task in enumerate(tasks, start=1):
            print(f"{x}. {task['title']}: {task['status']}")
    
        task_number = int(input("\nEnter the task number to delete: "))
        if task_number <= 0 or task_number > len(tasks):
            raise IndexError
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['title']} is deleted.")
    except (ValueError, IndexError):
        print("Invaid task number. Plesae enter a valid number.")

def app():
    while True:
        menu()
        try:
            choice = int(input("Please select an option from 1 to 5: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Quitting the application. Thank you for using task app.")
                break
            else:
                print("Invalid entry. Please select an option from 1 to 5.")
        except ValueError:
            print("Invalid entry. Please select an option from 1 to 5.")

app()
