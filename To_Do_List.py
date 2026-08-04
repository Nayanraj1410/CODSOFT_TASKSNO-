tasks = []

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")

    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for index, t in enumerate(tasks, start=1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{index}. {t['task']} [{status}]")

    elif choice == '3':
        if not tasks:
            print("No tasks to update.")
        else:
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_number - 1]["task"] = new_task
                print(f"Task {task_number} updated successfully.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        if not tasks:
            print("No tasks to delete.")
        else:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == '5':
        if not tasks:
            print("No tasks to mark.")
        else:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as complete.")
            else:
                print("Invalid task number.")

    elif choice == '6':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
