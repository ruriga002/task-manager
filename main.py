from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def main():
    tasks = []

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            add_task(tasks, title, description, due_date)

        elif choice == 2:
            if len(tasks) == 0:
                print("No tasks available.")
                continue

            print("\nTask List:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['title']} ({status})")

            try:
                task_index = int(
                    input("Enter task index to mark as complete: ")
                ) - 1

                mark_task_as_complete(tasks, task_index)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == 3:
            view_pending_tasks(tasks)

        elif choice == 4:
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}%")

        elif choice == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()