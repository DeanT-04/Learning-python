import os

def todo_list():
    # Define the filename for storing tasks
    filename = "todo.txt"

    def delete_task(tasks, index):
        # Remove the task at the specified index
        del tasks[index]
        # Write the updated tasks back to the file
        with open(filename, "w") as file:
            file.writelines(tasks)

    while True:
        # Display the main menu
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task
            task = input("Enter your task: ")
            # Append the new task to the file
            with open(filename, "a") as file:
                file.write(task + "\n")

        elif choice == "2":
            # View all tasks
            with open(filename, "r") as file:
                tasks = file.readlines()
                # Display tasks with numbering
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task.strip()}")

        elif choice == "3":
            # Delete a task
            with open(filename, "r") as file:
                tasks = file.readlines()
                # Display tasks with numbering
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task.strip()}")
                
                while True:
                    print("\nEnter the number of the task to delete, or '0' to go back:")
                    task_number = input()
                    if task_number == '0':
                        break
                    try:
                        # Convert input to integer and adjust for zero-based indexing
                        task_index = int(task_number) - 1
                        if 0 <= task_index < len(tasks):
                            # Delete the task if the index is valid
                            delete_task(tasks, task_index)
                            print(f"Task {task_number} has been deleted.")
                            break
                        else:
                            print("Invalid task number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        elif choice == "4":
            # Exit the program
            break

        else:
            print("Invalid choice")

# Run the todo list program
todo_list()