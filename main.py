from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)

def main():

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Add task
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            add_task(title, description, due_date)

        # Mark complete
        elif choice == "2":

            if len(tasks) == 0:
                print("No tasks available.")
                continue

            print("\nTask List:")
            for i, task in enumerate(tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['title']} ({status})")

            try:
                index = int(input("Enter task index to mark as complete: "))
                mark_task_as_complete(index)

            except ValueError:
                print("Error: Invalid task index.")

        # View pending
        elif choice == "3":
            view_pending_tasks()

        # Progress
        elif choice == "4":
            progress = calculate_progress()
            print(f"Task Completion Progress: {int(progress)}%")

        # Exit
        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()